---
name: incident-flow
description: '"장애 대응 시작" 요청 시 수집→분석→초안→검증 전체 단계를 지휘'
---
# Incident Flow — 조율 스킬(지휘자)

## 단계 — 순서 고정 · 산출물 없으면 다음 단계 금지
1. 수집  → log-digest 스킬      → `output/digest.md`
2. 분석  → root-cause 스킬      → `output/analysis.md`
3. 초안  → incident-report 스킬 → `output/report.md`
4. 검증  → report-check 스킬    → `output/verdict.md`

## 진행 규칙
- 각 단계 완료 시 **단계명과 산출물 경로만 한 줄** 보고한다.
- 이전 단계 산출물이 이미 있으면 그 단계는 건너뛴다.
  (중간부터 재개 가능 — 사건 ③의 원리)
- 단계 실패 시: 실패 지점과 사유를 보고하고 멈춘다.

## 금지
- 단계 건너뛰기 · 순서 변경 · 산출물 없이 "완료" 보고
