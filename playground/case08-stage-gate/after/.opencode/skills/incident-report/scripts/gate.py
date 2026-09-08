#!/usr/bin/env python3
"""단계 게이트 — 이전 산출물의 필수 섹션·최소 길이·미완성 표시를 검사한다.

약속(⑥)은 파일의 겉(경로·형식·RUN·SOURCE — 맞는 파일이 왔는가)을 본다.
이 예제 게이트(⑧)는 파일의 속(필수 항목이 채워졌는가 — 그 파일로 다음 일을 시작할 수 있는가)을 본다.
의미·수치·근거는 검사하지 않는다. 진행·반려는 종료코드를 받은 호출 측이 결정한다.
사용: python3 gate.py output/analysis.md
종료코드: PASS=0, FAIL=1 (스킬은 FAIL이면 진행하지 않는다)
"""
import re
import sys
from pathlib import Path

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
        text = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        print(f"GATE FAIL — 입력 파일 읽기 실패: {path}")
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
        print("→ 분석 보완 후 재시도. (호출 측에서 종료코드 1을 확인하고 진행을 중단해야 함)")
        return 1
    print(f"GATE PASS {checked}/{checked} — 필수 섹션·최소 길이·미완성 표시 검사 통과. 의미·근거 검증은 별도.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("사용법: python3 gate.py <analysis.md 경로>")
    raise SystemExit(main(sys.argv[1]))
