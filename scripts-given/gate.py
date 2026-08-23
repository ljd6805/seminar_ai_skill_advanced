#!/usr/bin/env python
# 게이트 판정기 (Lv.10 제공물) — 분석 산출물의 '내용'을 검사합니다
# 사용법: python .opencode/skills/incident-report/scripts/gate.py output/analysis.md
# 약속(⑥)이 파일의 겉모습(경로·형식)을 본다면, 게이트(⑧)는 안이 채워졌는지를 봅니다.
import sys

REQUIRED_SECTIONS = ["## 원인 후보", "## 재현 절차", "## 영향 범위"]
PLACEHOLDERS = ["TBD", "TODO"]


def section_body(text, name):
    """해당 섹션부터 다음 '## ' 전까지의 본문 줄들"""
    lines = text.splitlines()
    body, on = [], False
    for ln in lines:
        if ln.strip().startswith("## "):
            on = ln.strip().startswith(name)
            continue
        if on:
            body.append(ln.strip())
    return [b for b in body if b]


def main():
    if len(sys.argv) < 2:
        print("사용법: python gate.py <분석파일>")
        sys.exit(2)
    path = sys.argv[1]
    try:
        text = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        print("GATE: FAIL")
        print(f"  - 파일이 없습니다: {path} → 분석 단계를 먼저 실행하세요")
        sys.exit(1)

    problems = []
    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            problems.append(f"섹션 '{sec}' 이 없습니다")

    repro = section_body(text, "## 재현 절차")
    if not problems:
        if len(repro) < 2:
            problems.append("'## 재현 절차' 섹션이 비어 있거나 너무 짧습니다(2줄 이상)")
        for word in PLACEHOLDERS:
            if any(word in ln for ln in repro):
                problems.append(f"'## 재현 절차' 에 {word} 가 남아 있습니다 — 실제 절차로 채우세요")

    if problems:
        print("GATE: FAIL")
        for p in problems:
            print(f"  - {p}")
        print("  → 진행하지 않습니다. 분석 단계로 반려하세요 (부족 항목 위에 명시).")
        sys.exit(1)

    print(f"GATE: PASS (검사 {len(REQUIRED_SECTIONS)}/{len(REQUIRED_SECTIONS)} 통과)")
    sys.exit(0)


if __name__ == "__main__":
    main()
