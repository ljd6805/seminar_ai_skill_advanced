---
name: log-digest
description: 리그레션·크래시 로그의 요약, 오류 집계, 원인 분석 요청 시 사용
---
# Log Digest

## 절차
1. 로그 파일을 **직접 읽지 않는다**. (1,000줄 초과 시 반드시)
2. `python3 .opencode/skills/log-digest/scripts/digest.py <로그경로>` 를 실행한다.
   - 출력: 유형별 건수 · 첫 발생/첫 급증 시각 · 대표 사례 · TOTAL (약 30줄)
3. 스크립트 출력만 근거로 원인 후보를 2~3개 적는다.
4. 수치는 출력의 숫자를 그대로 옮긴다. (직접 세지 않는다)
5. `output/digest.md` 로 저장한다. 끝줄: `DIGEST-VERSION: 1`

## 금지
- 원본 로그의 READ, 부분 발췌 붙여넣기
- 스크립트 출력에 없는 수치의 사용 (직접 세지 않는다)

## 검증
- digest.md 의 유형별 건수 합 = 스크립트 TOTAL 값

## 폴더 구성
log-digest/ ├─ SKILL.md └─ scripts/digest.py  ← 컨텍스트 밖에서 실행
