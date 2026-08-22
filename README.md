# seminar_ai_skill_advanced

AI Agent 팀 세미나 시리즈 **4편 — SKILL 심화** 의 발표 자료 저장소입니다.

> **핵심 메시지**: 스킬 하나는 절차를 담고, 스킬 시스템은 한계를 설계한다 — **256k는 벽이 아니라 설계 조건이다.**

## 시리즈 위치

| 편 | 주제 | 형식 | 저장소 |
|---|---|---|---|
| 1편 | AI Agent 기본 개념 (Agent · Skill · MCP · Harness) | 이론 | [seminar_ai_agent](https://github.com/ljd6805/seminar_ai_agent) |
| 2편 | Skill Quest — Skill 실습 | 게임형 실습 | [seminar_ai_skill_quest](https://github.com/ljd6805/seminar_ai_skill_quest) |
| 3편 | Hook & Harness | 이론 + 실습 | [seminar_ai_hook_harness_slide](https://github.com/ljd6805/seminar_ai_hook_harness_slide) |
| **4편** | **SKILL 심화 — 기법 카탈로그** | 이론 + 실습(기획 중) | 본 저장소 |

## 4편 구성

- **이론편 — 기법 카탈로그** (90분 목표): **14개의 사건**을 사건당 두 장으로 푼다 — **문제 장**(구체적 문제 예시 재현 → 문제제기 → 원인 분석)과 **해결 장**(같은 요청의 해결 리플레이 → 스킬구성 → 기술소개). 기법의 이름은 항상 마지막에, 답으로서 등장한다.
  - **PART 1 · 컨텍스트 절약술** ①레퍼런스 계층화 ②스크립트 위임 ③외부 기억 ④지도 우선 탐색 ⑤분업 요약 — 사내 LLM의 **256k 컨텍스트** 제약을 설계 조건으로 삼는 다섯 사건
  - **PART 2 · 스킬 연계술** ⑥산출물 계약 ⑦파이프라인 스킬 ⑧라우터 스킬 ⑨게이트 체크 — 여러 스킬을 하나의 프로세스로 조립 (+ 결합 데모 시네마)
  - **PART 3 · 검증·리뷰 하네스** ⑩자가 리뷰 루프 ⑪반박 검증 ⑫기계 채점 하네스 ⑬증거 기반 완료 — 3편 Harness의 Validation·Record·Gate 를 스킬 안으로 (+ 네 겹 그물 정리)
  - **PART 4 · 확산** ⑭스킬 팩토리 — 기법을 팀의 기본값으로 배포
- **실습편 — Skill Quest 심화 시즌** (별도 기획, 방식 미정): 기존 [skill quest 리포](https://github.com/ljd6805/seminar_ai_skill_quest)의 데이터·채점기·보드 위에 심화 미션 트랙을 얹는 방향. 해결 장의 스킬구성이 미션 골격이 된다.

## 문서

| 문서 | 설명 |
|---|---|
| [`docs/seminar-synopsis.md`](docs/seminar-synopsis.md) | 이론편 시놉시스 v0.3 — 핵심 메시지, 전개 원칙(사건 서사), 사건 카탈로그(문제 예시→원인→해결), 장별 구성, 시간 배분, 실습 연계 계획, 결정 기록. **슬라이드 작성의 기준 문서** |
| [`slides/index.html`](slides/index.html) | 이론편 슬라이드 v0.3 (48장, 단일 흐름) — reveal.js 자립형(오프라인 동작), 1·2·3편과 동일한 테마 상속(Wanted Sans Variable + JetBrains Mono 임베드). 사건마다 문제·해결 리플레이 애니메이션과 원인 차트 포함 |

GitHub Pages 활성화 시: `https://ljd6805.github.io/seminar_ai_skill_advanced/slides/`

## 진행 상태

- [x] 주제 선정 및 기법 카탈로그 확정 (14기법 · 4파트)
- [x] 이론편 논리 구조 확정 (문제 주도형 사건 서사 — 문제예시→문제제기→원인분석→해결→기술소개)
- [x] 시놉시스 v0.3
- [x] 이론편 슬라이드 v0.3 (48장 — 2편 5이론 복습 · 사건 14건 × [문제·해결] 리플레이, 256k 가계부·파이프라인 시네마·결함 낙하 그물 애니메이션, 선택 지도·종합 사례·부록 요약표)
- [ ] 슬라이드 검토·보강 ← **다음 단계**
- [ ] 리허설 및 시간 조정
- [ ] 실습편 (Skill Quest 심화 시즌) 기획 — 미션 구성·레벨 체계·일정

## 작성 원칙

슬라이드는 `docs/seminar-synopsis.md` 의 장 구조를 그대로 따른다. 시놉시스와 슬라이드가 어긋나면 시놉시스를 먼저 갱신한다.
