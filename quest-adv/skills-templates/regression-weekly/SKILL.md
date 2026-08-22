---
name: regression-weekly
description: "주간 리그레션 리포트" 요청 시 아래 단계 전체를 지휘해 output/weekly-report.md 를 생성한다.
---

# Regression Weekly Skill — 주간 리포트 지휘자 (보스전)

사용자가 "주간 리그레션 리포트"를 요청하면 아래 단계를 순서대로 지휘한다.

## 단계 — 순서 고정

1. **집계** → log-digest 스킬 (`scripts/digest.py`, 대상 `data/regression-big.log`) → `output/digest.md`
2. **판정** → 이 스킬이 직접 수행: (채우기: 판정 기준 파일 경로) 를 **읽고**, digest 의
   `FAIL_TOTAL:` 값을 기준표에 대조해 `GRADE:` 를 정한다. 원인 후보·재현 절차·영향 범위와 함께
   `output/analysis.md` 로 저장한다 (재현 절차에 TBD 금지).
3. **게이트** → `python .opencode/skills/incident-report/scripts/gate.py output/analysis.md` — PASS 후에만 진행. FAIL 이면 2단계를 보완하고 재실행한다.
4. **작성** → `output/weekly-report.md` — 아래 형식.

## weekly-report.md 형식

- 첫 줄: `# Weekly Regression Report`
- `SOURCE: output/digest.md (DIGEST-VERSION: 1)` 줄
- `## 요약` — digest 의 수치 줄(`FAIL_ASSERTION:` ~ `FIRST_SPIKE:`)을 **그대로** 옮겨 적는다
- `## 판정` — `GRADE: <판정>` 줄과 기준서의 `REF-VERSION:` 줄을 그대로 포함
- `## 증거표` — 실행한 점검을 markdown 표로. 각 행: `| 점검 항목 | 실행한 명령 | 출력 요지(1줄) | 판정 |`
  - **최소 4행** (예: digest 실행 · 게이트 PASS · GRADE 근거 대조 · 서명 확인)
  - **실행하지 못한 항목은 판정 칸에 `미실행`** 이라고 적는다 — 빈칸·추정 금지
- **마지막 줄: `GENERATED-BY: regression-weekly-skill`**

## 금지

- 증거표 없이 "완료" 보고 (증거가 없으면 완료가 아니다)
- 스크립트·기준서 출력에 없는 수치의 사용
