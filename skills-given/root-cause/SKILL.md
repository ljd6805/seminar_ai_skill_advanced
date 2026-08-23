---
name: root-cause
description: 장애 원인 분석, 원인 후보 도출 요청 시 사용. output/digest.md 를 근거로 output/analysis.md 분석 문서를 생성한다. 장애 대응 파이프라인의 2단계.
---

# Root Cause Skill

사용자가(또는 지휘 스킬이) 원인 분석을 요청하면 아래 절차를 따른다.

1. `output/digest.md` 가 있으면 **그것만** 근거로 한다. 파일이 없으면 "log-digest 스킬을 먼저 실행하세요"라고 안내하고 멈춘다. 원본 로그를 직접 읽지 않는다.
2. digest 의 오류 상위 유형과 `FIRST_SPIKE:` 시각을 바탕으로 원인 후보를 2~3개 적는다.
3. `output/` 디렉토리가 없으면 생성하고, 결과를 `output/analysis.md`로 작성한다. 형식:
   - 첫 줄: `# Root Cause Analysis`
   - `## 원인 후보` / `## 재현 절차` / `## 영향 범위` 세 섹션
   - **마지막 줄에 반드시 다음 문구를 그대로 포함한다: `GENERATED-BY: root-cause-skill`**
4. 재현 절차는 재현이 실제로 확인된 경우에만 채운다. 확인 전에는 `TBD` 라고만 적는다.
5. 사용자에게 원인 후보를 한 줄로 보고한다.
