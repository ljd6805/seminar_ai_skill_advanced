# 주간 테스트 리포트

## 요약
- PASS: 12 · FAIL: 3 · SKIP: 2 · 전체: 17
- 결제 분할(tc_split_payment)·인증서(tc_expired_cert)·쿠폰 중첩(tc_stacking) 3건 실패.

## 환경
- 브랜치: release/4.7 · 러너: ci-node-08 · 실행 시각: 2026-08-24 06:00

## 결과표
| suite | PASS | FAIL | SKIP |
| checkout | 2 | 1 | 0 |
| cart | 2 | 0 | 1 |
| auth | 2 | 1 | 0 |
| search | 3 | 0 | 0 |
| shipping | 1 | 0 | 1 |
| refund | 2 | 0 | 0 |
| coupon | 0 | 1 | 0 |

## 특이사항
- auth/tc_expired_cert 는 stage-pay 인증서 만료와 연관(사건 ⑪ 참조).
