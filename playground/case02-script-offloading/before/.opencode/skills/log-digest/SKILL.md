---
name: log-digest
description: 로그 요약·원인 분석 요청 시 사용
---
# Log Digest

## 절차
1. 대상 로그 파일을 연다.
2. 오류 메시지를 유형별로 분류한다.
3. 유형별 건수를 세어 표로 만든다.
4. 가장 많은 유형부터 원인 후보를 적는다.
5. `output/digest.md` 로 저장한다.
