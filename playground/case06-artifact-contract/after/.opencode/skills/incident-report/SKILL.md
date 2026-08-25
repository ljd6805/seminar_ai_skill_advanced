---
name: incident-report
description: 장애 리포트 작성 시 사용 (digest.md 를 입력으로)
---
# Incident Report (소비자)

## 절차
1. `output/digest.md` 가 있으면 **그것만** 근거로 쓴다.
2. 버전 표시(`DIGEST-VERSION`)가 없으면 **옛 파일·복사본으로 간주**하고 쓰지 않는다.
3. 파일이 없으면 log-digest 실행을 안내하고 **멈춘다**.
4. 직접 로그를 읽지 않는다. (내용의 품질 검사는 이 약속의 몫이 아니다 — 사건 ⑧)
5. 리포트를 `output/report.md` 로 저장한다.

## 읽는 쪽 약속 (요약)
- 입력 경로: `output/digest.md` (고정)
- 버전 없으면 사용 거부 · 파일 없으면 정지
