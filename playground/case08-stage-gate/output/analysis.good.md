# 장애 분석

## 원인 후보
- stage-pay 인증서 만료(CN=stage-pay)로 payments 타임아웃 연쇄. 배포와 무관.

## 재현 절차
1. stage-pay 로 TLS 핸드셰이크 시도: `openssl s_client -connect stage-pay:443`
2. 인증서 notAfter 확인 → 만료일이 장애 시각 이전인지 대조.
3. 만료 인증서로 결제 호출 시 CertificateError 재현.

## 영향 범위
- 02:11~02:20 payments 전 구간 타임아웃. 결제 성공률 0%. 인증·게이트웨이 회로 개방.
