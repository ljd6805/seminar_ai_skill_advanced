---
name: api-migration
description: 모듈 API 마이그레이션(v1→v2) 작업·재개 요청 시 사용
---
# API Migration

## 절차
1. 시작할 때 `output/state.md` 가 있으면 **먼저 읽고 이어서** 한다.
   없으면 `assets/state-template.md` 를 복사해 만든다.
2. 이번에 다룰 모듈 하나를 정하고, 규칙(state.md 상단)을 확인한다.
3. 모듈을 v2 규칙으로 수정한다. (아래 "v2 규칙" 참조)
4. 끝나는 즉시 state.md 를 갱신한다:
   - 해당 줄 `[ ]` → `[x]`
   - 특이 사항은 "메모" 절에 1줄
5. 대화가 길어지면 **대화가 아니라 state.md 를 기준**으로 삼는다.

## v2 규칙
- `client.call(path, body)` → `client.request("POST", path, json=body)`
- `resp.data` → `resp.json()["data"]`
- `LegacyError` → `ApiError` 로 캐치 변경

## 금지
- state.md 갱신 없이 다음 모듈로 넘어가는 행위
- "아까 정한 규칙"처럼 대화 기억에 기대는 표현

## state.md 형식 (assets/state-template.md)
규칙: v2 통일 · [x] 01 · … · [ ] 40 · 메모: 03 API 변경 확인
