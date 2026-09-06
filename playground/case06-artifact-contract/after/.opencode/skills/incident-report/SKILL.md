---
name: incident-report
description: 장애 리포트 작성 시 사용 (digest.md 를 입력으로)
---
# Incident Report (소비자)

## 절차
1. 현재 요청의 RUN과 실제 입력 로그 해시를 먼저 확인한다. `output/digest.md`를 읽고 SCHEMA 지원 여부와 RUN·SOURCE의 일치를 검사한다.
2. 필드가 없거나 값이 다르면 입력 계약을 검증할 수 없으므로 사용을 보류하고 다시 생성한다. 형식 버전만으로 오래된 파일이라고 단정하지 않는다.
3. 파일이 없으면 log-digest 실행을 안내하고 **멈춘다**.
4. 검증된 digest를 기본 입력으로 쓴다. 내용의 정확성은 별도 검사 대상이며, 의문이 있으면 필요한 원본 근거를 확인한다. 사건 ⑧의 예제 게이트는 최소 형식 검사다.
5. 리포트를 `output/report.md` 로 저장한다.

## 읽는 쪽 약속 (요약)
- 입력 경로: `output/digest.md` (고정)
- SCHEMA 지원 여부 + 현재 요청의 RUN·SOURCE 일치 확인 · 파일 없으면 정지
