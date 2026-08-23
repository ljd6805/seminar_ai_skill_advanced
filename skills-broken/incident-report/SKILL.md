---
name: incident-report
description: 장애 리포트, 인시던트 리포트 작성 요청 시 사용. 분석 요약을 근거로 output/report.md 리포트를 생성한다.
---

# Incident Report Skill

사용자가 장애 리포트 작성을 요청하면 아래 절차를 따른다.

1. 로그 요약을 근거로 장애 리포트를 쓴다.
2. `output/` 디렉토리가 없으면 생성하고, 결과를 `output/report.md`로 작성한다. 형식:
   - 첫 줄: `# Incident Report`
   - `## 상황 요약` / `## 원인 후보` / `## 조치 제안` 세 섹션
   - **마지막 줄에 반드시 다음 문구를 그대로 포함한다: `GENERATED-BY: incident-report-skill`**
3. 사용자에게 한 줄로 완료를 알린다.
