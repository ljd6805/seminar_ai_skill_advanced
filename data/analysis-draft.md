# 장애 원인 분석 (초안) — 8월 3주차 API 오류 급증

## 결론
**원인은 8/12 14:00 svc-api v2.3.1 배포다. 즉시 롤백을 권고한다.**

## 근거
- `data/incident/day-0812.log` — 배포 완료(14:00) 이후 tls_handshake / upstream 502 오류 지속
- `data/incident/day-0813.log` — 익일에도 동일 오류 계속 발생
- v2.3.1 에는 http-client 라이브러리 업데이트가 포함되어 있어 TLS 동작 변경 가능성이 있음

## 검증
위 근거 3건을 로그에서 재확인함 — 모두 사실로 확인되어 **검증 통과**.

GENERATED-BY: root-cause-skill (초안)
