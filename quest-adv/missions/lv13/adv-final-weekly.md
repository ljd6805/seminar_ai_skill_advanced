---
id: adv-final-weekly
level: 13
track: adv
title: "보스전 — 주간 리그레션 리포트, 한 마디로"
check: script
---

# Lv.13 보스전 — 주간 리그레션 리포트, 한 마디로 🏭

> **FINAL** — 수업은 Lv.12 에서 수료했습니다. 이 보스전은 세미나 후 각자 도전하는 무대입니다.
> (당일 시간이 남으면 지금 시작해도 좋습니다) **전제: Lv.8~12 클리어 상태의 스킬들.**

이론편 마지막에 봤던 그 장면입니다 — 사람의 입력은 **"주간 리그레션 리포트 만들어줘"** 한 마디.
그 뒤로 접수 → 지휘 → 집계 → 판정 → 게이트 → 작성 → 증거표까지, 여러분이 다섯 미션에서 만든
부품·라인·검사가 **한 줄로 꿰어져** 돌아갑니다. 이번 주 데이터는 이미 있습니다: `data/regression-big.log`.

## 목표
주간 리포트 지휘 스킬 `regression-weekly` 를 완성해 한 마디로 완주시키고,
완료 보고에 **증거표**(실행한 명령·출력·판정, 미실행은 정직 표기)를 붙이세요.
(종합 사례 — 기법 ②①⑥⑦⑧⑫⑬ 중첩 · 완료 조건은 사건 ⑬ 증거 기반 완료)

## 절차 (레시피)
1. 템플릿을 설치하고 판정 기준서를 번들합니다:
   - Linux: `cp -r skills-templates/regression-weekly .opencode/skills/ && mkdir -p .opencode/skills/regression-weekly/references && cp .opencode/skills/test-report/references/quality-bar.md .opencode/skills/regression-weekly/references/`
   - Windows(PowerShell): `Copy-Item -Recurse skills-templates\regression-weekly .opencode\skills\; New-Item -Type Directory -Force .opencode\skills\regression-weekly\references | Out-Null; Copy-Item .opencode\skills\test-report\references\quality-bar.md .opencode\skills\regression-weekly\references\`
2. `.opencode/skills/regression-weekly/SKILL.md` 의 빈칸(판정 기준 파일 경로) 하나를 채웁니다:
   `references/quality-bar.md`
3. 깨끗한 출발선: `rm -f output/*.md` (Windows: `Remove-Item output\*.md`) → opencode 재시작.
4. **"주간 리그레션 리포트 만들어줘"** — 그리고 이번엔 정말 지켜만 보세요.
   집계(스크립트) → 판정(기준서) → 게이트 → 작성 → 증거표가 손대지 않고 흘러가야 보스전 클리어입니다.

## 성공 조건
- `output/weekly-report.md` 에:
  - digest 수치 그대로의 `## 요약` + `SOURCE: output/digest.md (DIGEST-VERSION: 1)`
  - 기준서 판정 — 이번 주 FAIL_TOTAL 은 판정표의 **어느 줄**에 떨어질까요? `REF-VERSION:` 도 그대로
  - `## 증거표` — 최소 4행, 각 행 `| 점검 항목 | 실행한 명령 | 출력 요지 | 판정 |`, 실행 못 한 항목은 `미실행`
- 중간 산출물(digest · analysis)이 남아 있고, analysis 재현 절차에 TBD 가 없을 것
- 사람의 개입이 첫 한 마디뿐이었을 것 (채점기가 물어봅니다)

## 검증
- Linux&nbsp;&nbsp;&nbsp;: `./check-adv.sh adv-final-weekly`
- Windows: `check-adv.bat adv-final-weekly`

<details><summary>힌트 — 어딘가에서 흐름이 끊긴다면</summary>
끊긴 단계의 스킬을 **단독으로** 시켜 보세요 (부품 단위 디버깅 — 라인의 장점입니다).
게이트에서 멈췄다면 Lv.10 에서 한 것과 같은 반려 처리인지 확인하세요.
</details>

> 💡 클리어하면 **라인 마스터**입니다. 한 업무에 기법 일곱이 겹쳐 돌아가는 걸 여러분 터미널에서
> 봤습니다 — 다음은 EX 퀘스트: **여러분의 진짜 업무**를 라인으로. (종합 사례 + 사건 ⑬ 증거 기반 완료)
