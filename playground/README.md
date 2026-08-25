# playground — 13기법 case별 체험 키트

이론편 슬라이드의 **각 사건(case)을 직접 손으로 돌려보기 위한** 개인 체험용 워크스페이스입니다.

> 📄 **한눈에 보는 HTML 가이드**: [`index.html`](index.html) — 13개 case의 요청 문장·관찰 포인트·심은 정답을
> 카드로 정리한 체험 가이드. GitHub Pages 활성화 시 `https://ljd6805.github.io/seminar_ai_skill_advanced/playground/`

> ⚠️ **이건 세미나 실습편(Skill Quest 심화 시즌)과는 별개입니다.**
> 시놉시스 §8 의 실습 연계 계획과 무관하며, 발표자가 혼자 기법을 체감해 보기 위한
> 비공식 부속물입니다. 실습편이 확정되면 그쪽은 별도 리포/트랙으로 갑니다.

## 구성 원칙

각 `caseNN-<기법>/` 폴더는 슬라이드의 [문제 → 해결] 구조를 그대로 옮겨,
**`before/`(문제의 스킬)** 와 **`after/`(해결된 스킬)** 를 나란히 둡니다.

- 스킬은 슬라이드의 Before/After 전문과 같은 형태의 실제 `SKILL.md` 입니다.
- `opencode` 기준(`.opencode/skills/<이름>/SKILL.md`)으로 배치했습니다. 원리는 도구 중립이라
  Claude Code 등 다른 스킬 도구에서도 SKILL.md 를 옮겨 그대로 체험할 수 있습니다.
- 스크립트가 필요한 기법(②⑧⑫)은 **실제로 동작하는 파이썬**을 넣었고, 데이터가 필요한
  기법(②③④⑤⑪⑫⑬)은 정답이 심긴 샘플/생성기를 넣었습니다.

## 체험하는 법 (공통)

1. 해당 case 의 `before/`(또는 `after/`)를 프로젝트 루트로 스킬 도구를 연다.
2. 각 폴더의 `README.md` 에 적힌 **요청 문장**을 그대로 입력한다.
3. **Before → After 순서로** 같은 요청을 넣고 차이를 관찰한다.
4. 스크립트 있는 case 는 에이전트 없이 스크립트만 먼저 돌려도 핵심이 보인다.
5. 모든 데이터는 `before/`·`after/` **안에** 들어 있다 — 워크스페이스 하나만 열면 자립적으로 돈다.
6. 스킬 발동·행동은 모델의 확률적 판단이라 회차마다 다를 수 있다.
   문제 장면이 그대로 재현되지 않아도 된다 — **before/after 스킬 구조의 차이**를 관찰하는 것이 목적이다.

전체를 원상복구하려면: `bash playground/reset.sh` (생성 산출물 삭제 + 체험 중 수정된 추적 파일 원복 — 실행 전 확인 프롬프트).

## 13기법 지도

### PART 1 · 컨텍스트 절약술 — "컨텍스트에는 결론만"

| # | case | 기법 | 한 줄 | 스크립트/데이터 |
|---|---|---|---|---|
| ① | `case01-progressive-disclosure` | 레퍼런스 계층화 | 목차만 싣고, 지식은 문 뒤에 | 규칙 references/ 3파일 |
| ② | `case02-script-offloading` | 스크립트 위임 | 세는 일은 코드가 | `digest.py` + 50만 줄 생성기 |
| ③ | `case03-external-memory` | 외부 기억 | 파일은 남는다 | 진행 중 `state.md` + 모듈 8개 |
| ④ | `case04-map-first` | 지도 우선 탐색 | 읽기는 검색의 결과 | 15k줄 repo(정답 심음) |
| ⑤ | `case05-fanout-summarize` | 분업 요약 | 쪼개면 곱해진다 | 취약점 심긴 모듈 6개 |

### PART 2 · 스킬 연계술 — 하나의 장애 대응 프로세스를 잇는 연작

| # | case | 기법 | 한 줄 | 스크립트/데이터 |
|---|---|---|---|---|
| ⑥ | `case06-artifact-contract` | 산출물 약속 | 약속이 있어야 부품 | digest.md 매개 · 장애 로그 |
| ⑦ | `case07-pipeline` | 파이프라인 스킬 | 프로세스도 스킬이다 | `incident-flow` 지휘자 + 부품 4개 |
| ⑧ | `case08-stage-gate` | 게이트 체크 | 약속이 형식이면 게이트는 내용 | `gate.py` + bad/good 분석 |
| ⑨ | `case09-router` | 라우터 스킬 | 접수 창구를 세워라 | `qa-desk` 분류표 + 스킬 4개 |

### PART 3 · 검증·리뷰 하네스 — "'됐습니다'를 '증명됐습니다'로"

| # | case | 기법 | 한 줄 | 스크립트/데이터 |
|---|---|---|---|---|
| ⑩ | `case10-self-review` | 자가 리뷰 루프 | 같은 모델, 다른 프레임 | 체크리스트 + diff + 약한 초안 |
| ⑪ | `case11-adversarial` | 반박 검증 | 무너뜨려 보라 | 반례(8/10) 심긴 service.log |
| ⑫ | `case12-script-judged` | 기계 채점 하네스 | 채점으로 통과하라 | `validate.py` + CSV(합계 17) |
| ⑬ | `case13-evidence-done` | 증거 기반 완료 | 증거 없으면 미완료 | 증거표 양식 + env(권한오류 심음) |

## 심은 정답 요약 (자가 채점용)

- ② AssertionError 1,842 · TimeoutError 317 · 첫 급증 02:14
- ④ 정답 흐름은 `repo/src/pay/validate.py` 의 `validatePayment`
- ⑤ 모듈별 취약점 6종(MD5·SQLi·path traversal·shell=True·약한 난수·하드코딩 비밀)
- ⑧ `analysis.bad.md` → GATE FAIL, `analysis.good.md` → GATE PASS
- ⑪ 8/10(배포 전)에 이미 CertificateError+Timeout 다수 → "8/12 배포" 결론은 기각
- ⑫ CSV 전체 17 = PASS 12 + FAIL 3 + SKIP 2 (`test-report.bad.md`→FAIL, `good`→PASS)
- ⑬ 4번 DB 항목은 권한 오류(errno 13) → "미실행" 정직 표기가 정답

## 스크립트만 빠르게 확인

```bash
# ② 로그 집계
cd case02-script-offloading/after && python3 tools/make_log.py --lines 50000 --out /tmp/r.log \
  && python3 .opencode/skills/log-digest/scripts/digest.py /tmp/r.log

# ⑧ 단계 게이트
cd case08-stage-gate/after \
  && python3 .opencode/skills/incident-report/scripts/gate.py output/analysis.bad.md \
  ;  python3 .opencode/skills/incident-report/scripts/gate.py output/analysis.good.md

# ⑫ 리포트 채점
cd case12-script-judged/after \
  && python3 .opencode/skills/test-report/scripts/validate.py output/test-report.bad.md \
  ;  python3 .opencode/skills/test-report/scripts/validate.py output/test-report.good.md
```
