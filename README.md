# seminar_ai_skill_advanced

AI Agent 팀 세미나 시리즈 **4편 — SKILL 심화** 의 저장소입니다 — **이론 슬라이드와 실습(SKILL QUEST 심화 시즌)을 모두 담습니다.** 실습은 이 리포 하나를 clone 하면 바로 시작됩니다 (2편 리포와 분리·독립).

> **핵심 메시지**: 스킬 하나는 절차를 담고, 스킬 시스템은 한계를 설계한다 — **256k는 벽이 아니라 설계 조건이다.**

## 시리즈 위치

| 편 | 주제 | 형식 | 저장소 |
|---|---|---|---|
| 1편 | AI Agent 기본 개념 (Agent · Skill · MCP · Harness) | 이론 | [seminar_ai_agent](https://github.com/ljd6805/seminar_ai_agent) |
| 2편 | Skill Quest — Skill 실습 | 게임형 실습 | [seminar_ai_skill_quest](https://github.com/ljd6805/seminar_ai_skill_quest) |
| 3편 | Hook & Harness | 이론 + 실습 | [seminar_ai_hook_harness_slide](https://github.com/ljd6805/seminar_ai_hook_harness_slide) |
| **4편** | **SKILL 심화 — 기법 카탈로그** | 이론 + 실습(기획 중) | 본 저장소 |

## 4편 구성

- **이론편 — 기법 카탈로그** (90분 목표): **13개의 사건**을 사건당 네 장으로 푼다 — **문제 장**(문제 예시 재현 → 문제의 스킬 원문 → 원인 분석), **해결 장**(해결 리플레이 → 해결된 스킬 발췌 → 기술소개), **원리 장**(기법의 작동 원리를 움직이는 다이어그램 한 장으로 — 스킬이 처음인 청중용), **Before/After 장**(고치기 전·후의 SKILL.md 전문 대조 — 스킬북의 본편). 기법의 이름은 항상 답으로서 마지막에 등장한다.
  - **PART 1 · 컨텍스트 절약술** ①레퍼런스 계층화 ②스크립트 위임 ③외부 기억 ④지도 우선 탐색 ⑤분업 요약 — 사내 LLM의 **256k 컨텍스트** 제약을 설계 조건으로 삼는 다섯 사건
  - **PART 2 · 스킬 연계술** ⑥산출물 약속 ⑦파이프라인 스킬 ⑧게이트 체크 ⑨라우터 스킬 — 하나의 장애 대응 프로세스를 네 사건으로 이어 완성하는 연작. 네 기법은 스킬과 스킬의 **연결**에 관한 네 질문(무엇을 주고받나·순서는·믿어도 되나·누가 나서나)에 답한다 (+ 연결의 네 질문 정리 · 결합 데모 시네마)
  - **PART 3 · 검증·리뷰 하네스** ⑩자가 리뷰 루프 ⑪반박 검증 ⑫기계 채점 하네스 ⑬증거 기반 완료 — 3편 Harness의 Validation·Record·Gate 를 스킬 안으로 (+ 네 겹 그물 정리 · "하나의 흐름" 정리 — P1 부품 → P2 라인 → P3 검사 연계)
  - ※ 확산(스킬 팩토리 — 기법을 팀의 기본값으로 배포)은 이번 세미나 범위에서 제외 — 추후 별도 다룬다
- **실습편 — SKILL QUEST 심화 시즌** (기획: [`docs/practice-seminar-plan.md`](docs/practice-seminar-plan.md)): **본 리포에 자체 수록** — 미션 트랙(Lv.8~13)·데이터·채점기·전용 웹 보드까지 이 리포 하나로 완결. 해결 장의 스킬구성이 미션 골격 — 본편 5미션(②·⑥·⑦+⑧·⑫·⑪) + 보스전(종합 사례+⑬ 증거표) + EX 자율 퀘스트, 120분 목표. 2편 [skill quest](https://github.com/ljd6805/seminar_ai_skill_quest)의 게임 형식(미션→채점→성장 코드→보드)을 계승하되 리포는 분리하며, 시즌 1 완주 상태는 세이브 파일(`skills-given/snapshot-s1/`)로 제공한다.

## 문서

| 문서 | 설명 |
|---|---|
| [`docs/seminar-synopsis.md`](docs/seminar-synopsis.md) | 이론편 시놉시스 v0.8 — 핵심 메시지, 전개 원칙(사건 서사), 사건 카탈로그(문제 예시→원인→해결), 장별 구성, 시간 배분, 실습 연계 계획, 결정 기록. **슬라이드 작성의 기준 문서** |
| [`slides/index.html`](slides/index.html) | 이론편 슬라이드 v0.8 (73장, 단일 흐름) — reveal.js 자립형(오프라인 동작), 1·2·3편과 동일한 테마 상속(Wanted Sans Variable + JetBrains Mono 임베드). 사건마다 문제·해결 리플레이 애니메이션, 원인 차트, **원리 도해 애니메이션**(목차와 본문·검문 게이트·창 분할 등 사건별 은유) 포함 |
| [`docs/practice-seminar-plan.md`](docs/practice-seminar-plan.md) | 실습편 기획 v0.4 — SKILL QUEST 심화 시즌. 3스테이지(부품→라인→검사)·6레벨(Lv.8~13) 미션 카탈로그, 초심자 가드레일, 채점·보드 설계, 당일 120분 운영안, 일정 로드맵. **실습 트랙의 기준 문서** |
| [`board/index.html`](board/index.html) | 실습 전용 웹 보드 — Lv.7(마스터)로 시작해 Lv.13(라인 마스터)까지. 성장 코드 입력·미션 카드·리캡·로봇 성장·도감 |
| `missions/` `data/` `tools/` `scripts-given/` `skills-*/` `check.sh(.bat/.ps1)` | 실습 트랙 실물 — 미션 카드 7장(Lv.8~13+EX), 함정 데이터, 제공 스크립트, 빈칸 템플릿, 시즌 1 세이브 파일, 채점기. [`answer-key/`](answer-key/)는 진행자용 (참가자 스포일러 주의) |

GitHub Pages 활성화 시: 슬라이드 `https://ljd6805.github.io/seminar_ai_skill_advanced/slides/` · 실습 보드 `https://ljd6805.github.io/seminar_ai_skill_advanced/board/` (루트 URL은 두 곳으로 안내하는 랜딩)

## 실습 시작하기 (SKILL QUEST 심화 시즌)

1. 이 레포를 clone 하고, 레포 최상위 폴더에서 opencode를 실행하세요.
2. [웹 보드](https://ljd6805.github.io/seminar_ai_skill_advanced/board/)에서 시즌 1의 에이전트 이름으로 등록하면 Lv.8 미션이 열립니다. (시작 레벨은 Lv.7 마스터)
3. 공통 준비(최초 1회): 시즌 1 세이브 파일 설치 — 명령은 Lv.8 미션 카드(`missions/lv8/`) 레시피 0번.
4. 게임 루프: 미션 수행(터미널) → `./check.sh <mission-id>` 채점 (Windows: `check.bat`) → 성장 코드 → 보드 입력 → 레벨업.
5. 수업 수료는 **Lv.12** 🎓 — 보스전(Lv.13)과 EX 자율 퀘스트(`missions/ex/`)는 세미나 후의 도전입니다.
6. 막히면 에이전트에게 물어보세요 — 반칙이 아니라 실무입니다. 스킬은 전부 이 레포의 `.opencode/skills/`(프로젝트 스코프)에 설치합니다.

## 진행 상태

- [x] 주제 선정 및 기법 카탈로그 확정 (13기법 · 3파트 — 확산(팩토리)은 범위 제외)
- [x] 이론편 논리 구조 확정 (문제 주도형 사건 서사 — 문제예시→문제제기→원인분석→해결→기술소개)
- [x] 시놉시스 v0.8
- [x] 이론편 슬라이드 v0.8 (73장 — 2편 5이론 복습 · 사건 13건 × [문제·해결·원리 도해·Before/After], PART 2 "연결의 네 질문" 정리, PART 3 마무리 "하나의 흐름"(부품→라인→검사) 파트 연계 정리, 256k 가계부·파이프라인 시네마·결함 낙하 그물 애니메이션, 선택 지도·종합 사례·부록 요약표)
- [ ] 슬라이드 검토·보강 ← **다음 단계**
- [ ] 리허설 및 시간 조정
- [x] 실습편 (SKILL QUEST 심화 시즌) 기획 v0.4 — 미션 구성(본편 5+보스전+EX)·레벨 체계(Lv.8~13)·운영안·초심자 가드레일, 일정은 D-기준 로드맵
- [x] 실습 트랙 본 리포 수록 (리포 분리 결정 반영) — 미션 카드·데이터·스크립트·템플릿·세이브 파일·채점기(`check.sh`), 전 미션 채점 경로 실행 검증
- [x] 실습 전용 웹 보드 (`board/`) — Lv.7 시작→Lv.13, Chromium 실기 테스트 통과
- [ ] 실습편 기획 리뷰 → v1.0 확정 (실습 일정 D 확정 포함)
- [ ] Windows 채점기(`check.bat/.ps1`) 실기 확인 (리허설에서)
- [ ] (정리) 2편 리포의 미사용 브랜치 `claude/season2-advanced-missions` 삭제 — 리포 분리 결정으로 폐기됨, GitHub 웹에서 삭제 (여기 세션에선 원격 브랜치 삭제가 차단됨)

## 작성 원칙

슬라이드는 `docs/seminar-synopsis.md` 의 장 구조를 그대로 따른다. 시놉시스와 슬라이드가 어긋나면 시놉시스를 먼저 갱신한다.
