---
name: convention-review
description: diff·코드의 컨벤션 리뷰, 규칙 위반 점검 요청 시 사용
---
# Convention Review

## 절차
1. diff에서 파일 유형·키워드만 훑는다. (전체 정독 금지)
2. 해당하는 규칙 파일**만** 골라 읽는다:
   - 이름·구조 지적 필요        → `references/naming.md`
   - try/except·오류 코드       → `references/error-handling.md`
   - thread·mutex·lock·async    → `references/concurrency.md`
3. 읽은 규칙의 조항 번호를 근거로 지적한다. (예: concurrency §3.1)
4. 읽지 않은 규칙으로는 지적하지 않는다.

## 금지
- `references/` 전체를 한 번에 읽는 행위
- 규칙 원문의 본문 복사 (조항 번호와 한 줄 요지만 인용)

## 출력
- 지적 목록: `[조항] 파일:줄 — 위반 내용 (1줄)` 형식
- 마지막 줄에 "읽은 규칙 파일: <목록>" 을 보고한다.
