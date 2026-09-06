#!/usr/bin/env python3
"""교육용 리포트 형식·집계 검사. 의미나 CSV 자체의 진실성은 보증하지 않는다.

사용: python3 validate.py <report.md> [data/test_results.csv]
종료코드: 검사 통과=0, 실패 또는 입력 오류=1.
"""
import csv
import io
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REQUIRED = ("요약", "환경", "결과표", "특이사항")
STATUSES = ("PASS", "FAIL", "SKIP")


def sections(text, problems):
    """정확한 2단계 제목 아래의 본문을 분리하고 중복·공란을 확인한다."""
    matches = list(re.finditer(r"^##[ \t]+([^\n]+?)[ \t]*$", text, re.MULTILINE))
    result = {}
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        if title in result:
            problems.append(f"중복 섹션: {title}")
        result[title] = text[match.end():end].strip()
    for title in REQUIRED:
        if not result.get(title):
            problems.append(f"필수 섹션 누락 또는 빈 본문: {title}")
    if re.search(r"\b(?:TODO|TBD)\b", text, re.IGNORECASE):
        problems.append("미완성 표시 TODO/TBD")
    return result


def source_counts(source, problems):
    """CSV의 suite/case 식별자와 상태를 검증한 뒤 집계한다."""
    reader = csv.DictReader(io.StringIO(source))
    counts = defaultdict(Counter)
    if reader.fieldnames != ["suite", "case", "result"]:
        problems.append("CSV 헤더는 suite,case,result여야 함")
        return counts
    seen = set()
    for line, row in enumerate(reader, 2):
        if None in row or any(not v or not v.strip() for v in row.values()):
            problems.append(f"CSV {line}행: 빈 값 또는 열 수 오류")
            continue
        suite, case, status = (row[k].strip() for k in reader.fieldnames)
        key = (suite, case)
        if key in seen:
            problems.append(f"CSV 중복 테스트: {suite}/{case}")
        seen.add(key)
        if status not in STATUSES:
            problems.append(f"CSV {line}행: 미지원 상태 {status}")
        else:
            counts[suite][status] += 1
    if not seen:
        problems.append("CSV에 테스트 결과가 없음")
    return counts


def summary_counts(body, problems):
    result = {}
    for label in (*STATUSES, "전체"):
        found = re.findall(rf"(?<!\w){label}\s*[:=]\s*([^\s·,;]+)", body)
        if len(found) != 1 or not re.fullmatch(r"[0-9]+", found[0]):
            problems.append(f"요약 {label}: 음이 아닌 정수 1개를 명시해야 함")
        else:
            result[label] = int(found[0])
    if len(result) == 4 and sum(result[s] for s in STATUSES) != result["전체"]:
        problems.append("요약 합계 불일치: PASS+FAIL+SKIP ≠ 전체")
    return result


def table_counts(body, problems):
    rows = [line.strip() for line in body.splitlines() if line.strip().startswith("|")]
    if not rows or [c.strip() for c in rows[0].strip("|").split("|")] != ["suite", *STATUSES]:
        problems.append("결과표 헤더는 suite | PASS | FAIL | SKIP이어야 함")
        return {}
    result = {}
    for row in rows[1:]:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        if len(cells) == 4 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if (not row.endswith("|") or len(cells) != 4 or not cells[0]
                or not all(re.fullmatch(r"[0-9]+", cell) for cell in cells[1:])):
            problems.append(f"결과표 빈 셀·열 수·정수 오류: {row}")
            continue
        if cells[0] in result:
            problems.append(f"결과표 중복 suite: {cells[0]}")
        result[cells[0]] = dict(zip(STATUSES, map(int, cells[1:])))
    return result


def validate(report, source):
    problems = []
    parts = sections(report, problems)
    expected = source_counts(source, problems)
    summary = summary_counts(parts.get("요약", ""), problems)
    table = table_counts(parts.get("결과표", ""), problems)
    totals = {status: sum(row[status] for row in expected.values()) for status in STATUSES}
    for label, value in {**totals, "전체": sum(totals.values())}.items():
        if label in summary and summary[label] != value:
            problems.append(f"원본 CSV와 요약 불일치: {label}={summary[label]}, 원본={value}")
    if set(table) != set(expected):
        problems.append("원본 CSV와 결과표의 suite 목록 불일치")
    for suite in table.keys() & expected.keys():
        if any(table[suite][status] != expected[suite][status] for status in STATUSES):
            problems.append(f"원본 CSV와 결과표 불일치: {suite}")
    return problems


def main(path, source_path="data/test_results.csv"):
    try:
        report = Path(path).read_text(encoding="utf-8")
        source = Path(source_path).read_text(encoding="utf-8-sig")
        problems = validate(report, source)
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"FAIL — 입력 읽기 오류: {exc}")
        return 1
    if problems:
        print(f"FAIL — {len(problems)}개 항목 지적")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("PASS — 필수 섹션·요약 합계·원본 CSV와 요약 및 suite별 결과표 대조 통과")
    print("범위: 입력 CSV 기준의 형식·집계 검사. 환경·원인 해석·원본의 진실성은 별도 검토.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit("사용법: python3 validate.py <report.md> [data/test_results.csv]")
    raise SystemExit(main(*sys.argv[1:]))
