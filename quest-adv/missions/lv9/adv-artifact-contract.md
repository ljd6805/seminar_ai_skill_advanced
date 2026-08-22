---
id: adv-artifact-contract
level: 9
track: adv
title: "전달 사고 — 두 스킬에 약속을 한 절씩"
check: script
---

# Lv.9 전달 사고 — 두 스킬에 약속을 한 절씩 🤝

> **STAGE 2 · 라인** — 부품은 준비됐습니다. 이제 스킬과 스킬을 **잇습니다**.

새 스킬 `incident-report`(장애 리포트 작성)가 팀에 들어왔습니다. 그런데 써 보면 이상합니다 —
digest 결과가 버젓이 있는데 리포트 스킬은 **그게 어디 있는지 모릅니다**. 사람이 대화에서 복사해
붙여 줘야 하고, 옛 파일을 집어 쓰는 사고도 납니다. 두 스킬 사이에 **약속이 없기 때문**입니다.

## 목표
새 스킬을 만들지 않습니다 — **이미 있는 두 스킬에 약속을 한 절씩** 적습니다.
log-digest 에는 **쓰는 쪽 약속**(경로·형식·버전)을, incident-report 에는 **읽는 쪽 약속**(그것만 근거로·버전 확인·없으면 정지)을. (사건 ⑥ 산출물 약속)

## 절차 (레시피)
1. 새(고장) 스킬을 설치합니다:
   - Linux: `cp -r skills-broken/incident-report .opencode/skills/`
   - Windows(PowerShell): `Copy-Item -Recurse skills-broken\incident-report .opencode\skills\`
2. `.opencode/skills/log-digest/SKILL.md` 절차 3~4번을 아래로 교체합니다 (**쓰는 쪽 약속** — 형식이 생깁니다):

   ```
   3. 결과를 output/digest.md 로 저장한다 (경로 고정). 형식:
      - `## 요약` — 스크립트 수치 줄(TOTAL_LINES ~ FIRST_SPIKE)을 그대로
      - `## 오류 Top 10` — TOP STACKS 상위 10줄
      - `## 이상 징후` — FIRST_SPIKE 전후의 특징 1~2줄
   4. 파일 끝의 두 줄: `DIGEST-VERSION: 1` 그리고 `GENERATED-BY: log-digest-skill`
   ```
3. `.opencode/skills/incident-report/SKILL.md` 절차 1번을 아래 1~4번으로 교체합니다 (**읽는 쪽 약속**):

   ```
   1. output/digest.md 가 있으면 **그것만** 근거로 쓴다. 원본 로그를 직접 읽지 않는다.
   2. 파일 안에 DIGEST-VERSION 줄이 없으면 **옛 파일·복사본으로 간주**하고 쓰지 않는다.
   3. 파일이 없으면 "log-digest 스킬을 먼저 실행하세요"라고 안내하고 **멈춘다**.
   4. 리포트 둘째 줄에 `SOURCE: output/digest.md (DIGEST-VERSION: 1)` 을 적고,
      원인 1위 유형과 건수는 digest 의 수치를 그대로 인용한다.
   ```
4. opencode 재시작.
5. **약속의 '정지' 조항부터 시험합니다** — 일부러 파일이 없는 상태를 만드세요:
   - Linux: `rm -f output/digest.md` / Windows: `Remove-Item output\digest.md`
   - 에이전트에게: **"장애 리포트 만들어줘"** → 리포트를 쓰지 않고 **멈추며 log-digest 실행을 안내**해야 합니다. (이 장면을 채점기가 물어봅니다)
6. 이제 정상 경로: **"대형 리그레션 로그 원인 분석해줘"** → 새 3섹션 형식의 digest.md 확인 → **"장애 리포트 만들어줘"** → `output/report.md` 확인.

## 성공 조건
- `output/digest.md` 가 3섹션(`## 요약` / `## 오류 Top 10` / `## 이상 징후`) + `DIGEST-VERSION: 1`
- `output/report.md` 에 `SOURCE: output/digest.md (DIGEST-VERSION: 1)` 줄과 digest 근거 수치, 스킬 서명
- 파일이 없을 때 리포트 스킬이 **멈추는** 것을 직접 확인했을 것

## 검증
- Linux&nbsp;&nbsp;&nbsp;: `./check-adv.sh adv-artifact-contract`
- Windows: `check-adv.bat adv-artifact-contract`

<details><summary>힌트 — 에이전트가 멈추지 않고 로그를 직접 읽으러 간다면</summary>
읽는 쪽 약속의 3번("없으면 안내하고 멈춘다")과 1번의 "직접 읽지 않는다"가 본문에 정말 있는지,
고친 뒤 재시작했는지 확인하세요. 스킬은 본문에 적힌 만큼만 약속을 지킵니다.
</details>

> 💡 이 약속이 책임지는 건 **전달까지**입니다 — 맞는 파일이, 맞는 자리에, 맞는 모양으로.
> 내용이 부실한 경우는 별개의 사건이고, 다음 미션의 **게이트**가 맡습니다. (사건 ⑥, 그리고 예고 ⑧)
