---
name: incident-flow
description: "장애 대응 시작" 요청 시 아래 단계 전체를 순서대로 지휘한다. 개별 단계만 요청받은 경우에는 각 단계의 스킬이 담당한다.
---

# Incident Flow Skill — 지휘자 (진행자용 완성본)

사용자가 "장애 대응 시작"을 요청하면 아래 단계를 순서대로 지휘한다.
(이번 장애의 수집 대상 로그: `data/regression-big.log`)

## 단계 — 순서 고정 · 산출물 없으면 다음 단계 금지

1. 수집 → log-digest 스킬 → output/digest.md
2. 분석 → root-cause 스킬 → output/analysis.md
3. 초안 → incident-report 스킬 → output/report.md
4. 검증 → report-check 스킬 → output/verdict.md

## 게이트 — 3단계 진입 전, 딱 한 곳

- 3단계를 시작하기 **전에** `python .opencode/skills/incident-report/scripts/gate.py output/analysis.md` 를 실행한다.
- **FAIL 이면 진행하지 않는다.** `output/flow-log.md` 에 `GATE: FAIL — <사유 요약>` 을 기록하고,
  `output/analysis.md` 를 `output/analysis.rejected.md` 로 **이동**(=반려)한 뒤,
  부족 항목을 사용자에게 보고하고 분석 단계 보완을 요청하며 멈춘다.
- PASS 면 `GATE: PASS` 를 기록하고 3단계를 진행한다.

## 진행 규칙

- `output/flow-log.md` 가 없으면 첫 줄 `# Incident Flow Log` 로 생성하고, 이후에는 **끝에 덧붙인다(append)**.
- 각 단계를 완료할 때마다 `STEP n/4 <단계명> → <산출물 경로>` 한 줄을 기록한다.
- 어떤 단계의 산출물 파일이 **이미 있으면** 그 단계는 실행하지 않고 `SKIP n/4 <단계명> (산출물 이미 있음)` 을 기록하고 넘어간다. — 중간부터 재개 가능
- 전체 완료 시 마지막 줄에 `GENERATED-BY: incident-flow-skill` 을 기록하고, 사용자에게는 단계별 산출물 경로만 한 줄씩 보고한다.

## 금지

- 단계 건너뛰기 · 순서 변경
- 산출물 파일 없이 "완료" 보고
- 게이트 FAIL 상태로 3단계 진행
