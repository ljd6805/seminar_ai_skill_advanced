---
name: incident-report
description: 장애 리포트 초안 작성 시 사용
---
# Incident Report — 3단계(초안)

## 절차
1. `output/digest.md` 를 근거로 개요·타임라인을 쓴다.
   (없으면 log-digest 실행을 안내하고 멈춘다)
2. `output/analysis.md` 가 있으면 원인·조치 섹션의 근거로 삼는다.
   없으면 이 파이프라인의 필수 입력이 없으므로 분석 단계로 돌려보내고 중단한다.
3. `output/report.md` 로 저장한다.

## 입력·출력 추적
incident-flow의 현재 RUN·SOURCE와 입력 계약을 확인한다. 필드 누락·불일치나 필수 입력 부재 시 중단한다. 출력에 SCHEMA: 1, RUN, SOURCE와 실제 입력 산출물 해시(INPUT)를 남긴다. 파일 존재만으로 이전 실행 결과를 재사용하지 않는다.
