#!/usr/bin/env python3
"""테스트 리포트 채점기 — 결정적 기준(형식·합계·금지문구)을 코드로 판정한다.

말로 하는 검토는 확률적으로 놓친다. 채점은 같은 입력이면 같은 판정.
사용: python3 validate.py output/test-report.md
종료코드: PASS=0, FAIL=1
"""
import re
import sys

REQUIRED_SECTIONS = ["요약", "환경", "결과표", "특이사항"]
BANNED = ["아마", "대충", "완벽히", "TODO", "TBD"]


def find_int(text: str, label: str):
    m = re.search(rf"{label}\s*[:=]?\s*(\d+)", text)
    return int(m.group(1)) if m else None


def main(path: str) -> int:
    try:
        text = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        print(f"FAIL — 리포트 파일 없음: {path}")
        return 1

    problems = []

    # 1) 필수 섹션
    for s in REQUIRED_SECTIONS:
        if not re.search(rf"^#{{1,6}}\s*{re.escape(s)}", text, re.MULTILINE):
            problems.append(f"필수 섹션 누락: '{s}'")

    # 2) 합계 일치 (PASS + FAIL + SKIP == 전체)
    p, f_, s_, total = (find_int(text, k) for k in ("PASS", "FAIL", "SKIP", "전체"))
    if None in (p, f_, s_, total):
        problems.append(f"수치 누락 (PASS={p} FAIL={f_} SKIP={s_} 전체={total})")
    elif p + f_ + s_ != total:
        problems.append(f"합계 불일치: PASS {p}+FAIL {f_}+SKIP {s_} = {p+f_+s_} ≠ 전체 {total}")

    # 3) 금지 문구 / 빈 표 셀
    for b in BANNED:
        if b in text:
            problems.append(f"금지 문구 사용: '{b}'")
    if re.search(r"\|\s*\|\s*\|", text):
        problems.append("결과표에 빈 셀(| |)이 있음")

    if problems:
        print(f"FAIL — {len(problems)}개 항목 지적")
        for pb in problems:
            print(f"  - {pb}")
        return 1
    print(f"PASS — 필수 섹션 {len(REQUIRED_SECTIONS)}개 · 합계 {p}+{f_}+{s_}={total} 일치 · 금지 문구 없음")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("사용법: python3 validate.py <리포트.md 경로>")
    raise SystemExit(main(sys.argv[1]))
