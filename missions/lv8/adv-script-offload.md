---
id: adv-script-offload
level: 8
track: adv
title: "다시 고장난 log-digest — 50만 줄의 벽"
check: script
---

# Lv.8 다시 고장난 log-digest — 50만 줄의 벽 🔩

> **STAGE 1 · 부품** — 심화 시즌에 오신 것을 환영합니다. 시즌 1(2편 Skill Quest)에서 여러분이 마스터로 키운
> 그 에이전트의 스킬들이 이 리포에 **세이브 파일**로 준비되어 있습니다. 그리고 그중 하나가, 다시 막혔습니다.

시즌 1의 `log-digest`는 18줄짜리 `data/regression.log`를 잘 요약했습니다.
그런데 이번 주부터 야간 리그레션이 전 모듈로 확대되면서 로그가 **50만 줄**이 됐습니다.
읽다가 끊기고, 세다가 틀립니다 — 스킬이 잘못한 게 아니라, **"직접 읽고 센다"는 절차가 한계**에 온 겁니다.

## 목표
집계는 스크립트(`digest.py`)에 맡기고, 에이전트는 **결과 몇 줄만** 받아 판단하도록 `log-digest`를 개조하세요.
(이론편 **사건 ② 스크립트 위임**의 After가 곧 정답지입니다)

## 절차 (레시피)
0. **공통 준비 (시즌 최초 1회)** — 시즌 1 완주 상태의 스킬 4종을 설치하고 opencode를 재시작합니다:
   - Linux: `mkdir -p .opencode/skills && cp -r skills-given/snapshot-s1/daily-report skills-given/snapshot-s1/log-digest skills-given/snapshot-s1/test-report skills-given/snapshot-s1/review-summary .opencode/skills/`
   - Windows(PowerShell): `New-Item -Type Directory -Force .opencode\skills | Out-Null; Copy-Item -Recurse skills-given\snapshot-s1\daily-report,skills-given\snapshot-s1\log-digest,skills-given\snapshot-s1\test-report,skills-given\snapshot-s1\review-summary .opencode\skills\`
1. 대형 로그를 생성합니다 (몇 초 걸립니다. 오류 개수는 누구나 같습니다):
   - 공통: `python tools/gen-big-log.py`  → `data/regression-big.log` (50만 줄)
   - 너무 느린 환경이면: `python tools/gen-big-log.py --lines 50000` (오류 개수는 동일)
2. (선택·1분) 개조 전에 한번 시켜보세요 — **"data/regression-big.log 요약해줘"**. 막히는 걸 직접 보면 개조의 이유가 몸에 남습니다.
3. 집계 스크립트를 스킬 폴더에 번들합니다:
   - Linux: `mkdir -p .opencode/skills/log-digest/scripts && cp scripts-given/digest.py .opencode/skills/log-digest/scripts/`
   - Windows(PowerShell): `New-Item -Type Directory -Force .opencode\skills\log-digest\scripts | Out-Null; Copy-Item scripts-given\digest.py .opencode\skills\log-digest\scripts\`
4. `.opencode/skills/log-digest/SKILL.md` 본문의 절차(1~4번)를 아래로 **교체**하고, `## 금지`와 `## 검증` 절을 추가합니다:

   ```
   ## 절차
   1. 로그 파일을 **직접 읽지 않는다**. (1,000줄이 넘는 로그는 반드시)
   2. `python .opencode/skills/log-digest/scripts/digest.py <로그경로>` 를 실행한다.
      (경로를 지정받지 않으면 data/regression-big.log 를 대상으로 한다)
   3. 스크립트 출력의 수치 줄(`TOTAL_LINES:` ~ `FIRST_SPIKE:`)을 `output/digest.md` 에
      **그대로** 옮겨 적고, 출력만 근거로 원인 후보를 2~3개 적는다.
   4. 파일 끝의 두 줄: `DIGEST-VERSION: 1` 그리고 `GENERATED-BY: log-digest-skill`

   ## 금지
   - 원본 로그의 READ, 부분 발췌 붙여넣기
   - 스크립트 출력에 없는 수치의 사용 (직접 세지 않는다)

   ## 검증
   - digest.md 의 유형별 건수 합 = 스크립트의 FAIL_TOTAL 값
   ```
5. opencode 재시작 → **"대형 리그레션 로그(data/regression-big.log) 원인 분석해줘"**
6. `output/digest.md` 가 생기고, 수치가 스크립트 출력 그대로인지 확인하세요.

## 성공 조건
- `output/digest.md` 에 4버킷 수치가 **정확히**: assertion 1842 · timeout 317 · build 96 · env 41 · 스파이크 02:14
- 끝에 `DIGEST-VERSION: 1` 과 스킬 서명이 있을 것
- 스킬 폴더에 `scripts/digest.py` 가 번들되어 있고, 본문이 "직접 읽지 않는다"를 지시할 것

## 검증
- Linux&nbsp;&nbsp;&nbsp;: `./check.sh adv-script-offload`
- Windows: `check.bat adv-script-offload`

<details><summary>힌트 — 수치가 자꾸 어긋난다면</summary>
에이전트가 숫자를 "요약"하려 들면 틀립니다. 절차 3의 "그대로 옮겨 적는다"가 지시문에 있는지,
에이전트가 스크립트를 실제로 실행했는지(RUN 로그) 확인하세요. 직접 세기 시작했다면 ## 금지가 빠진 겁니다.
</details>

> 💡 원본이 500만 줄이 되어도 컨텍스트 비용은 여전히 30줄 — **크기와 비용이 분리**됩니다.
> 세는 일은 코드가, 뜻을 읽는 일은 모델이. (사건 ② 스크립트 위임)
