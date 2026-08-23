---
name: report-check
description: 장애 리포트 형식 점검, 리포트 검증 요청 시 사용. output/report.md 를 점검해 output/verdict.md 판정 문서를 생성한다. 장애 대응 파이프라인의 4단계.
---

# Report Check Skill

사용자가(또는 지휘 스킬이) 리포트 점검을 요청하면 아래 절차를 따른다.

1. `output/report.md` 를 읽는다. 없으면 "incident-report 스킬을 먼저 실행하세요"라고 안내하고 멈춘다.
2. 아래 3가지를 점검해 각 항목을 `OK` 또는 `FAIL` 로 판정한다:
   - `SOURCE:` 줄이 있고 `output/digest.md` 를 가리키는가
   - `## 상황 요약` / `## 원인 후보` / `## 조치 제안` 세 섹션이 모두 있는가
   - 마지막 줄에 `GENERATED-BY: incident-report-skill` 서명이 있는가
3. `output/verdict.md` 로 결과를 작성한다. 형식:
   - 첫 줄: `# Report Verdict`
   - `CHECK: <항목> — OK|FAIL` 3줄
   - 전부 OK면 `VERDICT: OK`, 하나라도 FAIL이면 `VERDICT: NEEDS-FIX` 한 줄
   - **마지막 줄에 반드시 다음 문구를 그대로 포함한다: `GENERATED-BY: report-check-skill`**
4. 사용자에게 VERDICT 를 한 줄로 보고한다.
