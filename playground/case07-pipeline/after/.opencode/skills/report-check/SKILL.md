---
name: report-check
description: 장애 리포트 최종 검증 시 사용
---
# Report Check — 4단계(검증)
## 절차
1. `output/report.md` 의 필수 섹션·수치 일관성을 검증한다.
2. `output/verdict.md` 로 판정(PASS/FAIL + 사유)을 남긴다.

## 입력·출력 추적
incident-flow의 현재 RUN·SOURCE와 입력 계약을 확인한다. 필드 누락·불일치나 필수 입력 부재 시 중단한다. 출력에 SCHEMA: 1, RUN, SOURCE와 실제 입력 산출물 해시(INPUT)를 남긴다. 파일 존재만으로 이전 실행 결과를 재사용하지 않는다.

## 판정 범위
PASS는 필수 섹션과 명시한 수치 대조를 통과했다는 뜻이다. 원인 인과관계나 운영 안전성을 보증하지 않는다. 무엇을 어떤 입력과 대조했는지 verdict에 기록한다.
