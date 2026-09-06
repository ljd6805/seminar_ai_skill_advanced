---
name: log-digest
description: 리그레션·크래시 로그의 요약, 오류 집계, 원인 분석 요청 시 사용
---
# Log Digest

## 절차
1. 큰 로그는 먼저 집계한다. 필요한 원문 범위는 이후 좁혀 확인한다.
2. `python3 .opencode/skills/log-digest/scripts/digest.py <로그경로>` 를 실행한다.
   - 출력: 유형별 건수 · 첫 발생/첫 급증 시각 · 대표 사례 · TOTAL (출력 길이는 오류 유형·입력에 따라 달라짐)
3. 집계 출력으로 원인 후보를 2~3개 세우고, 필요하면 관련 원문·누락 범위를 확인한다.
4. 수치는 출력의 숫자를 그대로 옮긴다. (직접 세지 않는다)
5. `output/digest.md` 로 저장한다. 끝줄: `DIGEST-VERSION: 1` (형식 버전이며 데이터 최신성 표시는 아님)

## 금지
- 목적 없이 원본 로그 전체를 컨텍스트에 반복해서 싣기
- 스크립트 출력에 없는 수치의 사용 (직접 세지 않는다)

## 검증
- digest.md 의 유형별 건수 합 = 스크립트 TOTAL 값

## 폴더 구성
log-digest/ ├─ SKILL.md └─ scripts/digest.py  ← 컨텍스트 밖에서 실행
