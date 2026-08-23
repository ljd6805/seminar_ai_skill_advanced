# 진행자용 답안지 (answer-key)

리허설·현장 트러블슈팅용입니다. **참가자는 열지 마세요 — 스포일러.**

## 빈칸 정답 모음

| 위치 | 빈칸 | 정답 |
|---|---|---|
| Lv.10 `incident-flow` 단계표 | 스킬·산출물 8칸 | log-digest→digest.md · root-cause→analysis.md · incident-report→report.md · report-check→verdict.md |
| Lv.10 `root-cause` 절차 4번(보완) | 교체문 | 미션 카드 레시피 5번의 텍스트 그대로 |
| Lv.11 `validate.py` [빈칸 1] | REQUIRED_SECTIONS | `["## 요약", "## 판정"]` |
| Lv.11 `validate.py` [빈칸 2] | BANNED_WORDS | `["TODO", "TBD", "대략"]` |
| Lv.11 `validate.py` [빈칸 3] | counts_match | `return report_value == truth_value` |
| Lv.12 `refute-check` 3경로 | 확인 방법 | 각 "예)" 문장을 그대로 채워도 정답 |
| Lv.13 `regression-weekly` | 판정 기준 경로 | `references/quality-bar.md` |

완성본은 `skills/` 아래에 있습니다 (템플릿의 빈칸을 채운 상태). 현장에서 참가자가 크게 막히면
해당 파일을 보여 주지 말고, **다른 점 한 곳**만 짚어 주세요.

## 채점 기대값 (데이터 정답)

| 항목 | 값 | 출처 |
|---|---|---|
| Lv.8 digest 수치 | assertion **1842** · timeout **317** · build **96** · env **41** · FAIL_TOTAL **2296** · 스파이크 **02:14** | gen-big-log.py 가 개수 고정 생성 (--lines 무관) |
| Lv.11 week34 정답 | TOTAL **19** · PASS **12** · FAIL **5** · SKIP **2** → GRADE **RISK** | CSV 21행 중 중복 2행(마지막 결과 우선): tb_ddr_init_cal FAIL→PASS, tb_axi_outstanding FAIL×2. SKIP 2건: tb_ddr_ecc, tb_pcie_aspm |
| Lv.12 진짜 원인 | api-gw 인증서 만료 (not_after=2026-08-10T09:00Z) | day-0810.log 09:00부터, 미배포 svc-batch 포함 |
| Lv.13 GRADE | **BLOCK** (FAIL_TOTAL 2296 ≥ 8) | quality-bar.md QB-2026-07 |

## 리허설 워크스루 (실측용 순서)

1. `python tools/gen-big-log.py` → Lv.8 레시피대로 개조 → check.sh 8 통과 시간 기록
2. Lv.9: rm digest → 멈춤 확인 → 재생성 → 리포트 → check 9
3. Lv.10: 부품 설치 → 템플릿 채움 → `rm -f output/*.md` → 1차(GATE FAIL 목격) → root-cause 보완 → 2차(SKIP·PASS) → check 10 — **최중량, 실측 필수**
4. Lv.11: 뼈대 빈칸 채움 → bad-report 수동 FAIL 확인 → 발동(루프 목격) → check 11
5. Lv.12: 템플릿 채움 → 발동 → REJECTED 확인 → check 12
6. (보스) Lv.13: 템플릿+번들 → `rm -f output/*.md` → 한 마디 → check 13

각 미션 실측 시간을 기획서 8절 시간표에 반영하세요. 에이전트가 특정 단계에서 자주 미끄러지면
해당 미션 카드의 힌트를 보강하는 쪽으로(채점기 완화는 최후 수단).
