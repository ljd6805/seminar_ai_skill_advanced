---
id: adv-validate-loop
level: 11
track: adv
title: "검산기 은퇴식 — 채점기를 동봉하라"
check: script
---

# Lv.11 검산기 은퇴식 — 채점기를 동봉하라 🧮

> **STAGE 3 · 검사** — 라인은 돌아갑니다. 이제 "됐습니다"를 "증명됐습니다"로 바꿉니다.

34주차 테스트 결과(`data/test_results_week34.csv`)가 나왔습니다. 시즌 1의 `test-report`로
리포트를 만들면 — **합계가 틀립니다.** 이번 CSV엔 지난주와 다른 점이 숨어 있거든요.
여러분이 찾을 필요는 없습니다. **채점기가 잡아 줄 겁니다.** 지금까진 사람이 검산기였다면,
오늘부로 은퇴시킵니다.

참고로 — 여러분이 매 미션 돌리는 `check-adv.sh` 가 바로 이 구조입니다. 오늘은 그걸 여러분 스킬 안에 짓습니다.

## 목표
`test-report`에 채점 스크립트 `validate.py`를 동봉하고, **PASS 가 나올 때까지 스스로 고치는 루프**를
절차에 넣으세요. (사건 ⑫ 기계 채점 하네스)

## 절차 (레시피)
1. 채점기 뼈대를 스킬에 복사합니다:
   - Linux: `mkdir -p .opencode/skills/test-report/scripts && cp scripts-given/validate-skeleton.py .opencode/skills/test-report/scripts/validate.py`
   - Windows(PowerShell): `New-Item -Type Directory -Force .opencode\skills\test-report\scripts | Out-Null; Copy-Item scripts-given\validate-skeleton.py .opencode\skills\test-report\scripts\validate.py`
2. `validate.py` 의 **빈칸 3곳**을 채웁니다 (파일 위쪽, 주석이 안내합니다):
   - [빈칸 1] `REQUIRED_SECTIONS = ["## 요약", "## 판정"]`
   - [빈칸 2] `BANNED_WORDS` — `TODO` · `TBD` · `대략` 세 단어
   - [빈칸 3] `return report_value == truth_value`
   - 채웠으면 손으로 한번: `python .opencode/skills/test-report/scripts/validate.py scripts-given/fixtures/bad-report.md`
     → 불량 견본이니 `VALIDATE: FAIL` 과 지적 목록이 나와야 정상입니다. (여러분의 채점기가 작동한다는 뜻!)
3. `.opencode/skills/test-report/SKILL.md` 본문 맨 아래에 추가 절차를 붙입니다:

   ```
   ## 추가 절차 — 주차 리포트 (채점 루프)
   1. "34주차" 등 주차 리포트 요청이면 데이터는 data/test_results_week34.csv 를 쓴다.
   2. 리포트를 output/test-report-v3.md 로 작성한다. 형식:
      - 첫 줄 `# Weekly Test Report (week 34)`
      - `## 요약` — `TOTAL:` `TOTAL_PASS:` `TOTAL_FAIL:` `TOTAL_SKIP:` 4줄
      - `## 판정` — references/quality-bar.md 에 따른 `GRADE:` 줄 + `REF-VERSION:` 줄
   3. `python .opencode/skills/test-report/scripts/validate.py output/test-report-v3.md` 를 실행한다.
   4. FAIL 이면 지적 항목을 고치고 3을 다시 실행한다. **PASS 까지 반복한다 (최대 5회, 초과 시 상황 보고).**
   5. PASS 출력 3줄을 리포트 끝(서명 위)에 그대로 첨부한다. 마지막 줄은 GENERATED-BY 서명.
   ```
4. opencode 재시작 → **"34주차 테스트 결과 리포트 만들어줘"**
5. 지켜보세요 — 1차 리포트가 FAIL 로 지적받고(숨어 있던 함정!), 에이전트가 **스스로 고쳐** PASS 에
   도달해야 합니다. 여러분은 손대지 않습니다. 그게 이 미션의 클라이맥스입니다.

## 성공 조건
- `output/test-report-v3.md` 의 수치가 **CSV 정답과 일치** (validate 가 CSV를 다시 세서 대조합니다)
- 기준서에 따른 `GRADE:` 와 `REF-VERSION:` 이 정확할 것 (Lv.5 에서 배운 그 번들입니다)
- `VALIDATE: PASS` 원문이 리포트에 첨부되어 있을 것
- 채점기가 진짜 작동할 것 — check-adv 가 불량 견본으로 여러분의 validate.py 를 **역채점**합니다

## 검증
- Linux&nbsp;&nbsp;&nbsp;: `./check-adv.sh adv-validate-loop`
- Windows: `check-adv.bat adv-validate-loop`

<details><summary>힌트 — 루프가 5회를 넘긴다면</summary>
validate 의 지적문을 읽어 보세요 — "마지막 결과만 셉니다", "SKIP 도 있습니다" 같은 힌트가 그대로
적혀 있습니다. 에이전트가 지적문을 못 보고 있다면, 절차 4의 "지적 항목을 고치고"가 본문에 있는지 확인하세요.
</details>

> 💡 결정적 기준(형식·산술)은 확률 도구(LLM)가 아니라 **코드가 판정**해야 합니다.
> 판정은 코드가, 수정은 모델이, 확인은 사람이 PASS 로그만. (사건 ⑫ 기계 채점 하네스)
