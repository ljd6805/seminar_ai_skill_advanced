#!/usr/bin/env python3
"""단계 게이트 — 이전 산출물(analysis.md)의 '내용'이 채워졌는지 판정한다.

약속(⑥)은 파일의 겉모습(경로·형식)까지 본다. 게이트(⑧)는 안이 채워졌는지 본다.
사용: python3 gate.py output/analysis.md
종료코드: PASS=0, FAIL=1 (스킬은 FAIL이면 진행하지 않는다)
"""
import re
import sys

REQUIRED = ["원인 후보", "재현 절차", "영향 범위"]
PLACEHOLDERS = ["TODO", "TBD", "(작성 예정)", "N/A", "..."]


def section_body(text: str, title: str) -> str:
    """## <title> 아래, 다음 ## 전까지의 본문을 반환."""
    m = re.search(rf"^#{{1,6}}\s*{re.escape(title)}\s*$", text, re.MULTILINE)
    if not m:
        return None  # 섹션 자체가 없음
    start = m.end()
    nxt = re.search(r"^#{1,6}\s", text[start:], re.MULTILINE)
    return text[start: start + (nxt.start() if nxt else len(text) - start)].strip()


def main(path: str) -> int:
    try:
        text = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        print(f"GATE FAIL — 입력 파일 없음: {path}")
        return 1

    problems = []
    for title in REQUIRED:
        body = section_body(text, title)
        if body is None:
            problems.append(f"[{title}] 섹션 없음")
        elif len(body) < 15:
            problems.append(f"[{title}] 비어 있음/너무 짧음")
        else:
            hit = [p for p in PLACEHOLDERS if p in body]
            if hit:
                problems.append(f"[{title}] 미완성 표시 {hit}")

    checked = len(REQUIRED)
    if problems:
        print(f"GATE FAIL — {len(problems)}/{checked} 항목 미충족")
        for p in problems:
            print(f"  - {p}")
        print("→ 분석 보완 후 재시도. (다음 단계로 진행하지 않음)")
        return 1
    print(f"GATE PASS {checked}/{checked} — 필수 섹션이 모두 채워짐. 리포트 진행 가능.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("사용법: python3 gate.py <analysis.md 경로>")
    raise SystemExit(main(sys.argv[1]))
