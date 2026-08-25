# 사건 ⑫ — 기계 채점 하네스 (Script-Judged Gate)

> 슬라이드: PART 3 · 사건 12 — "형식·합계 같은 기계적 실수는 말로 잡히지 않습니다"

## 시나리오
주간 테스트 리포트에서 PASS 12 + FAIL 3 = 15 인데 전체가 17(SKIP 2 누락).
"다시 확인해줘"로도 안 잡힌다 — 결정적 기준(합계)을 확률적 도구(말)로 검사한 탓.
정답: `data/test_results.csv` = 전체 17 (PASS 12·FAIL 3·SKIP 2).

## 먼저 채점기만 체험
```bash
cd after
python3 .opencode/skills/test-report/scripts/validate.py output/test-report.bad.md   # FAIL (합계·섹션·금지문구)
python3 .opencode/skills/test-report/scripts/validate.py output/test-report.good.md  # PASS
```

## 스킬로 체험
1. **Before** — `before/` test-report: "눈으로 스스로 한 번 검토"까지. 합계 실수를 말로 놓친다.
   - ※ 재현 장치("스크립트 금지 — 직접 세고 말로 검토") 포함 — 요즘 모델은 알아서
     검증 코드를 짜기 때문(그 우회가 바로 기법 ⑫다).
   - `data/test_results.csv 로 주간 리포트 써줘` → 합계·섹션 오류가 통과되는지 관찰.
2. **After** — `after/` test-report: validate.py 채점 루프 내장.
   - 같은 요청 → 작성 → 채점 FAIL(지적 항목) → 수정 → 재채점 → **PASS까지 반복(≤5회)** →
     PASS 로그 원문을 리포트 끝에 첨부.

## 관찰 포인트
- 판정이 코드(결정적)라 같은 입력이면 같은 판정 — 사람은 검산기가 아니라 PASS 로그만 확인.
- 사건 ②(스크립트 위임)의 교훈이 검증에도 적용된다 — 세는 일은 코드의 몫.
- 2편 실습의 `check.sh` 가 바로 이 구조였다.

**한 줄 정리 — 채점으로 통과하라.** 말로 통과하지 말고, PASS까지 스스로 고친다.
