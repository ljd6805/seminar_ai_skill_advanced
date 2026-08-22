---
id: adv-pipeline
level: 10
track: adv
title: "새벽 2시 훈련 — 지휘 스킬과 게이트 한 곳"
check: script
---

# Lv.10 새벽 2시 훈련 — 지휘 스킬과 게이트 한 곳 🚨

> **STAGE 2 · 라인** — 이번 미션이 심화 시즌의 최중량입니다. 시간을 넉넉히 쓰세요.

새벽 2시에 장애가 나면 우리 팀은 4단계로 대응합니다: **수집 → 분석 → 초안 → 검증**.
부품 스킬은 이제 다 있습니다. 그런데 **순서를 아는 스킬이 없습니다** — 신입은 다음 단계를 모르고,
시니어의 머릿속에만 조립 설명서가 있습니다. 그리고 하나 더: 부실한 분석이 그대로 리포트까지
흘러가는 사고도 막아야 합니다.

## 목표
① "장애 대응 시작해줘" **한 마디**로 4단계가 자동 진행되는 지휘 스킬 `incident-flow`를 완성하고
(사건 ⑦ 파이프라인 스킬), ② 부실이 비싸지는 길목 **딱 한 곳**(분석→초안 사이)에 게이트를 세웁니다
(사건 ⑧ 게이트 체크).

## 절차 (레시피)
1. 나머지 부품 2개와 게이트 판정기를 설치합니다:
   - Linux: `cp -r skills-given/root-cause skills-given/report-check .opencode/skills/ && mkdir -p .opencode/skills/incident-report/scripts && cp scripts-given/gate.py .opencode/skills/incident-report/scripts/`
   - Windows(PowerShell): `Copy-Item -Recurse skills-given\root-cause,skills-given\report-check .opencode\skills\; New-Item -Type Directory -Force .opencode\skills\incident-report\scripts | Out-Null; Copy-Item scripts-given\gate.py .opencode\skills\incident-report\scripts\`
2. 지휘 스킬 템플릿을 설치하고 **빈칸을 채웁니다**:
   - Linux: `cp -r skills-templates/incident-flow .opencode/skills/` / Windows: `Copy-Item -Recurse skills-templates\incident-flow .opencode\skills\`
   - `.opencode/skills/incident-flow/SKILL.md` 의 단계표 빈칸 8곳을 이 표대로:

     | 단계 | 스킬 | 산출물 |
     |---|---|---|
     | 1 수집 | log-digest | output/digest.md |
     | 2 분석 | root-cause | output/analysis.md |
     | 3 초안 | incident-report | output/report.md |
     | 4 검증 | report-check | output/verdict.md |

3. 깨끗한 출발선을 만들고 재시작합니다: `rm -f output/*.md` (Windows: `Remove-Item output\*.md`) → opencode 재시작.
4. **"장애 대응 시작해줘"** — 그리고 지켜보세요. 1, 2단계가 지나고 게이트에서 **FAIL 이 납니다.**
   (root-cause 가 재현 절차를 `TBD` 로 남기는 버릇이 있거든요 — 전임자의 "신중함"입니다)
   flow 는 analysis.md 를 `analysis.rejected.md` 로 **반려**하고, 부족 항목을 보고하며 멈춰야 합니다.
5. 반려 사유를 해소합니다 — `.opencode/skills/root-cause/SKILL.md` 절차 4번을 아래로 교체:

   ```
   4. 재현 절차에는 digest 의 FIRST_SPIKE 시각과 대표 오류 1건을 이용해
      "최소 재현 시나리오"를 3단계로 적는다. TBD/TODO 라고 적지 않는다.
   ```
6. 재시작 → 다시 **"장애 대응 시작해줘"**. 이번엔 이렇게 흘러야 합니다:
   `SKIP 1/4`(digest 가 이미 있으니 건너뜀 — **중간 재개**) → 분석 재실행 → `GATE: PASS` → 초안 → 검증.
   ※ output/ 을 지우지 말고 그대로 재요청하세요 — 건너뛰는 걸 봐야 합니다.

## 성공 조건
- `output/` 에 digest · analysis · report · verdict 4종 + `flow-log.md`
- flow-log 에 진행의 전 과정이 남을 것: `STEP 1/4` ~ `STEP 4/4`, `GATE: FAIL`(1차), `SKIP 1/4` 와 `GATE: PASS`(2차)
- 최종 analysis.md 의 재현 절차에 TBD 가 없을 것

## 검증
- Linux&nbsp;&nbsp;&nbsp;: `./check-adv.sh adv-pipeline`
- Windows: `check-adv.bat adv-pipeline`

<details><summary>힌트 ① — 한 마디에 4단계가 안 굴러간다면</summary>
incident-flow 의 description 에 "장애 대응 시작"이 있는지(트리거), 단계표의 스킬 이름·경로 빈칸이
표와 정확히 같은지 확인하세요. 지휘 스킬은 단계표에 적힌 만큼만 지휘합니다.
</details>
<details><summary>힌트 ② — 게이트 FAIL 후 재실행해도 계속 FAIL 이라면</summary>
반려(analysis.md → analysis.rejected.md 이동)가 됐는지 보세요. 부실 파일이 그 자리에 남아 있으면
"산출물 있으면 건너뜀" 규칙 때문에 분석이 다시 실행되지 않습니다 — 반려는 파일을 치우는 일까지입니다.
</details>

> 💡 게이트는 **모든 연결마다가 아니라, 부실의 대가가 커지는 길목에 한두 곳**입니다.
> 이 라인에도 딱 한 곳뿐이죠. 여기서 잡으면 수정 1×, 리포트까지 가면 3×, 배포 뒤엔 9×.
> (사건 ⑦ 파이프라인 · 사건 ⑧ 게이트 — 그리고 SKIP 은 사건 ③ 외부 기억의 원리입니다)
