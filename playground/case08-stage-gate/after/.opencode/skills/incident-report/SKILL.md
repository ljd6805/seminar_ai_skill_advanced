---
name: incident-report
description: 장애 리포트 작성 시 사용 (분석 산출물 게이트 포함)
---
# Incident Report

## 절차
1. 시작 전에 `python3 .opencode/skills/incident-report/scripts/gate.py output/analysis.md` 실행.
   - 검사: 필수 섹션(재현 절차·영향 범위·원인 후보)이 **실제로 채워졌는가**
     · TODO/TBD 없음
2. **FAIL → 진행하지 않는다.** 부족 항목을 그대로 알리고 분석 단계로 반려한다.
   - 형식: "GATE FAIL — [항목]. 분석 보완 후 재시도."
3. PASS → 리포트 작성을 시작한다.
4. `output/report.md` 저장 · PASS 로그를 리포트 끝에 첨부.

## 폴더 구성
incident-report/ ├─ SKILL.md └─ scripts/gate.py  ← 이전 산출물 판정기
