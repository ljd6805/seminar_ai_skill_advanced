---
name: root-cause
description: 장애 원인 분석 시 사용
---
# Root Cause — 2단계(분석)
## 절차
1. `output/digest.md` 를 근거로 원인 후보를 분석한다.
2. `output/analysis.md` 로 저장한다. (## 원인 후보 / ## 재현 절차 / ## 영향 범위)

## 입력·출력 추적
incident-flow의 현재 RUN·SOURCE와 입력 계약을 확인한다. 필드 누락·불일치나 필수 입력 부재 시 중단한다. 출력에 SCHEMA: 1, RUN, SOURCE와 실제 입력 산출물 해시(INPUT)를 남긴다. 파일 존재만으로 이전 실행 결과를 재사용하지 않는다.
