# quest-adv — SKILL QUEST 심화 시즌(Season 2) 스테이징

> ✅ **병합 완료 (2026-08-23)**: 이 트리는 실습 리포의 **`claude/season2-advanced-missions` 브랜치**에 반영되었습니다
> (+웹 보드 v2.0 Lv.8~13 확장 — 보드는 스테이징에 없고 그 브랜치에만 있습니다). 이후 수정은 그 브랜치에서 하고,
> 이 폴더는 출제 이력·기획 리뷰용 사본으로 유지합니다. 아래 "적용 방법"은 재병합이 필요할 때만 쓰세요.

4편 실습 세미나의 **출제물 초안**입니다. 기획서(`docs/practice-seminar-plan.md`)대로 만든
미션·데이터·스크립트·채점기 일습이며, 폴더 구조는 실습 리포
[`seminar_ai_skill_quest`](https://github.com/ljd6805/seminar_ai_skill_quest)의 최상위와 **1:1**입니다.

## 적용 방법 (실습 리포에 병합)

```bash
# seminar_ai_skill_quest 체크아웃 루트에서:
cp -r quest-adv/missions quest-adv/data quest-adv/tools quest-adv/scripts-given \
      quest-adv/skills-broken quest-adv/skills-given quest-adv/skills-templates \
      quest-adv/check-adv.sh quest-adv/check-adv.ps1 quest-adv/check-adv.bat \
      quest-adv/answer-key .
chmod +x check-adv.sh
echo "data/regression-big.log" >> .gitignore   # 생성 파일 — 커밋 금지 (50만 줄 ≈ 40MB)
```

- 기존 파일과 겹치는 이름 없음 (신규 추가만). `check.sh`는 건드리지 않고 시즌 2 채점기를 별도 파일로 둡니다.
- 성장 코드는 기초 시즌과 **같은 SALT·같은 방식** — 보드가 검증 로직 변경 없이 Lv.8~13 코드를 받을 수 있습니다.
- **남은 별도 작업**: 웹 보드 Lv.8~13 확장(미션 데이터·리캡·로봇 파츠·EX 도감 칸). 보드 확장 전에는 "코드 수첩"(진행자가 코드 수기 확인)으로 운영 가능.

## 구성

| 경로 | 내용 |
|---|---|
| `missions/lv8~lv13, ex/` | 미션 카드 7장 (`track: adv`) — Lv.8 스크립트 위임 · Lv.9 산출물 약속 · Lv.10 파이프라인+게이트 · Lv.11 채점 루프 · Lv.12 반박 검증 · Lv.13 보스전 · EX 자율 |
| `tools/gen-big-log.py` | Lv.8용 50만 줄 로그 생성기 — 오류 개수 고정(assertion 1842 · timeout 317 · build 96 · env 41 · 스파이크 02:14), `--lines` 로 줄여도 동일 |
| `scripts-given/` | 참가자 제공 스크립트 — digest.py(완성) · gate.py(완성) · validate-skeleton.py(빈칸 3곳) · fixtures/bad-report.md(역채점용) |
| `data/` | test_results_week34.csv(중복·SKIP 함정) · incident/ 5일치 로그(진짜 원인: 8/10 인증서 만료) · analysis-draft.md(그럴듯한 오답) |
| `skills-broken/incident-report/` | Lv.9 시작점 — 입력의 위치·형식이 미정인 스킬 |
| `skills-given/` | root-cause(재현 절차를 TBD로 남기는 함정 내장) · report-check(완성) · **snapshot-s1/**(시즌 1 완주 세이브 파일 — 미수료자용) |
| `skills-templates/` | 초심자용 빈칸 템플릿 — incident-flow · refute-check · regression-weekly |
| `check-adv.sh/.ps1/.bat` | 시즌 2 채점기 (Linux / Windows) — 통과 시 `GROW-L8~13-XXXX` 발급 |
| `answer-key/` | **진행자용** — 빈칸 정답·채점 기대값·리허설 워크스루·완성본 스킬 (참가자 스포일러 주의) |

## 설계 노트 (요약)

- **초심자 가드레일**: 신규 스킬은 전부 템플릿 빈칸 채우기(백지 작성 없음), 카드의 교체 텍스트는 복붙 가능,
  함정(주차 CSV·TBD 분석·그럴듯한 결론)은 참가자가 아니라 **게이트·채점기가 잡도록** 설계 — FAIL 메시지가 다음 행동을 알려줍니다.
- **의도된 FAIL 경험**: Lv.10의 게이트 반려(→`analysis.rejected.md` 이동 후 재실행 시 SKIP으로 중간 재개 체감),
  Lv.11의 1차 리포트 FAIL→자가 수정 루프. 채점기는 이 흔적(flow-log의 FAIL/SKIP/PASS, VALIDATE: PASS 첨부)을 요구합니다.
- **역채점**: Lv.11은 check-adv 가 참가자의 validate.py 를 불량 견본으로 먼저 채점합니다 — 채점기부터 채점에 합격.
