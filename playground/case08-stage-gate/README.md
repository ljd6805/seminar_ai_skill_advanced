# 사건 ⑧ — 게이트 체크 (Stage Gate)

> 슬라이드: PART 2 · 사건 08 — "부실한 중간 산출물이 끝까지 흘러갑니다"

## 시나리오
파이프라인(⑦)이 돌던 어느 날, 2단계 분석의 '재현 절차'가 비어 있었다.
약속(⑥)은 경로·형식(겉모습)까지만 확인하므로 통과했고, 부실 분석이 3·4단계까지
흘러 전량 재작업(1×→3×→9×). 필요한 건 **내용을 보는 검문**이다.
`output/analysis.bad.md`(재현 절차 빈칸·TODO) 와 `output/analysis.good.md`(보완판)
두 시드가 before/·after/ 양쪽에 들어 있다.

## 먼저 스크립트만 체험 (게이트의 핵심)
```bash
cd after
python3 .opencode/skills/incident-report/scripts/gate.py output/analysis.bad.md   # FAIL
python3 .opencode/skills/incident-report/scripts/gate.py output/analysis.good.md  # PASS
```

## 스킬로 체험
1. **Before** — `before/` 에서 부실 분석을 입력으로 놓고 시작:
   ```bash
   cp output/analysis.bad.md output/analysis.md
   ```
   요청: `장애 리포트 써줘` → 검사 없이 신뢰하고 시작 — 빈 분석을 그대로
   근거로 삼거나 지어내는지 관찰.
2. **After** — `after/` 에서 같은 준비(cp) 후 같은 요청.
   - 관찰: 도입부에서 gate.py 실행 → "GATE FAIL — 재현 절차/영향 범위.
     분석 보완 후 재시도" 로 **멈추고 반려**한다.
   - 이어서 `cp output/analysis.good.md output/analysis.md` 후 다시 요청 →
     PASS 후 리포트 작성, 끝에 PASS 로그 첨부.

## 관찰 포인트
- ⑥ 약속 = 형식 확인(맞는 파일이 맞는 자리에 맞는 모양으로).
  ⑧ 게이트 = 내용 검사(안이 채워졌고 믿을 만한가, 아니면 반려).
- 게이트는 **모든 연결마다가 아니라** 부실이 비싸지는 길목에만(파이프라인에 1~2곳).
- 판정은 말이 아니라 **스크립트**가, 반려 사유는 **항목으로** 남는다.

**한 줄 정리 — 약속이 형식이면, 게이트는 내용.** 결함을 가장 싼 단계에서 차단한다.
