---
name: log-digest
description: 리그레션·크래시·장애 로그의 요약, 오류 집계 요청 시 사용
---
# Log Digest (생산자)

## 절차
1. 로그를 요약한다.
2. 결과를 표로 정리한다.
3. 결과를 `output/digest.md` 로 저장한다. (경로 고정)
4. 형식: `## 요약` / `## 오류 Top 10` / `## 이상 징후`
5. 마지막 줄에 `DIGEST-VERSION: 1` 을 남긴다.
6. 사용자에게는 경로만 한 줄로 알린다.

## 쓰는 쪽 약속 (요약)
- 경로: `output/digest.md` (고정)
- 형식: 위 3개 섹션 고정
- 버전: 마지막 줄 `DIGEST-VERSION: 1`
