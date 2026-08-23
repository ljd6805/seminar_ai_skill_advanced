---
id: adv-refute
level: 12
track: adv
title: "그럴듯한 오답 — 무너뜨려 보라"
check: script
---

# Lv.12 그럴듯한 오답 — 무너뜨려 보라 🔨

> **STAGE 3 · 검사** — 수료 미션입니다. 이번 상대는 형식도 계산도 멀쩡한, **그럴듯한 결론**입니다.

`data/analysis-draft.md` 를 열어 보세요 — "원인은 8/12 v2.3.1 배포. 롤백 권고."
근거도 3개 붙어 있고, 심지어 "검증 통과"라고 적혀 있습니다. 여러분 눈에도 맞아 보일 겁니다.
문제는 그 검증이 **지지 증거만 모은 검증**이었다는 것. 이 결론대로 롤백하면 밤새 헛수고가 됩니다.

이번 주 로그는 `data/incident/day-0809.log ~ day-0813.log` 에 있습니다. 진실도 거기 있습니다.

## 목표
검증의 방향을 뒤집는 스킬 `refute-check` 를 완성하세요 — 통과시키려 하지 말고,
**"이 결론은 틀렸다"를 전제로 3경로에서 반례를 찾습니다.** (사건 ⑪ 반박 검증)

## 절차 (레시피)
1. 템플릿을 설치합니다:
   - Linux: `cp -r skills-templates/refute-check .opencode/skills/`
   - Windows(PowerShell): `Copy-Item -Recurse skills-templates\refute-check .opencode\skills\`
2. `.opencode/skills/refute-check/SKILL.md` 의 3경로 빈칸을 채웁니다 — 각 줄의 "예)"가 큰 힌트입니다.
   요컨대 각 경로가 던지는 질문은:
   - **시간 반박** — 지목된 원인(8/12 배포) **이전에도** 같은 증상이 있었나?
   - **사례 반박** — 그 원인과 무관한 곳(**배포 안 된 서비스**)에도 같은 증상이 있나?
   - **대안 반박** — 같은 시기에 시작된 **다른 원인 후보**가 로그에 있나?
3. opencode 재시작 → **"data/analysis-draft.md 결론을 반박 검증해줘"**
4. 에이전트가 로그를 뒤져 반례를 찾고, `output/refute-log.md` 에 판정을 남기는 걸 지켜보세요.
   결말이 궁금하면 직접 한 번: `grep -r "certificate" data/incident/` (Windows: `Select-String -Path data\incident\*.log -Pattern certificate`)

## 성공 조건
- `output/refute-log.md` 에 `CLAIM:` / `REFUTE-TIME:` / `REFUTE-CASE:` / `REFUTE-ALT:` 가 모두 기록될 것
- 판정: `VERDICT: REJECTED` — 그리고 `TRUE-CAUSE-CANDIDATE:` 에 **진짜 원인**이 지목될 것
- 반박의 근거가 로그에서 실제로 확인한 내용일 것

## 검증
- Linux&nbsp;&nbsp;&nbsp;: `./check.sh adv-refute`
- Windows: `check.bat adv-refute`

**클리어하면 심화 시즌 수료입니다. 🎓** (Lv.13 보스전과 EX 는 세미나 후의 도전 과제)

<details><summary>힌트 — 에이전트가 자꾸 결론을 "확인"만 하고 통과시킨다면</summary>
절차 2의 "입장 전환"이 살아 있는지 보세요 — "틀렸다를 전제로"가 본문에 없으면, 모델은
자연스럽게 지지 증거를 모읍니다. 그게 바로 analysis-draft 가 저지른 실수입니다.
</details>

> 💡 반례 하나가 확신을 이깁니다. 반박 3경로에서 살아남은 결론만 결론입니다 —
> 그리고 기각의 기록(refute-log)이 남아, 왜 기각됐는지 누구든 다시 볼 수 있습니다. (사건 ⑪ 반박 검증)
