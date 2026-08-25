# API Migration — 진행 상태 (state.md)

## 규칙 (첫 결정 — 절대 잊지 말 것)
- 전부 **v2 API 로 통일**한다. (v1 스타일로 되돌리지 않는다)
- 변환 규칙은 SKILL.md 의 "v2 규칙" 절을 단일 출처로 삼는다.

## 진행 체크리스트
- [x] 01 auth_client.py
- [x] 02 cart_client.py
- [ ] 03 payment_client.py
- [ ] 04 shipping_client.py
- [ ] 05 coupon_client.py
- [ ] 06 refund_client.py
- [ ] 07 search_client.py
- [ ] 08 catalog_client.py

## 다음 작업
- 다음 모듈: 03

## 메모 (모듈별 특이사항 1줄)
- 02 cart_client — 배열 응답도 resp.json()["data"] 로 통일함
