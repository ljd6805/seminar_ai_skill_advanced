---
name: log-digest
description: 장애 로그 수집·요약 시 사용
---
# Log Digest — 1단계(수집)
## 절차
1. logs/incident.log 를 요약한다.
2. `output/digest.md` 로 저장한다. (## 요약 / ## 오류 Top / ## 이상 징후)

## 입력·출력 추적
incident-flow의 현재 RUN·SOURCE와 입력 계약을 확인한다. 필드 누락·불일치나 필수 입력 부재 시 중단한다. 출력에 SCHEMA: 1, RUN, SOURCE와 실제 입력 산출물 해시(INPUT)를 남긴다. 파일 존재만으로 이전 실행 결과를 재사용하지 않는다.
