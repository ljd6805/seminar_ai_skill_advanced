---
name: incident-report
description: 장애 리포트 작성 시 사용 (분석 산출물 게이트 포함)
---
# Incident Report

## 절차
1. 시작 전에 `python3 .opencode/skills/incident-report/scripts/gate.py output/analysis.md` 실행.
   - 검사: 필수 섹션 3개(재현 절차·영향 범위·원인 후보), 각 본문 15자 이상, 미완성 표시 없음.
   - 이 검사는 의미·근거·원본 수치의 정확성을 판정하지 않는다.
2. **FAIL → 진행하지 않는다.** 부족 항목을 그대로 알리고 분석 단계로 반려한다.
   - 형식: "GATE FAIL — [항목]. 분석 보완 후 재시도."
3. PASS → 리포트 작성을 시작한다.
4. `output/report.md` 저장 · PASS 로그를 리포트 끝에 첨부.

## 폴더 구성
incident-report/ ├─ SKILL.md └─ scripts/gate.py  ← 이전 산출물 판정기

## 강제 실행의 경계
SKILL.md는 FAIL일 때 중단하도록 지시한다. gate.py는 종료코드만 반환하며 후속 도구 실행을 직접 차단하지 않는다. 강제 차단은 호출 실행기나 훅이 종료코드를 확인하도록 구성한다.
