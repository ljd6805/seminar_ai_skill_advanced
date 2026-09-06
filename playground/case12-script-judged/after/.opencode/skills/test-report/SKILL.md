---
name: test-report
description: 테스트 결과 집계·주간 리포트 작성 시 사용 (기계 채점 포함)
---
# Test Report

## 절차
1. `data/test_results.csv` 를 집계해 리포트를 `output/test-report.md` 로 작성한다.
   - 필수 섹션: `## 요약` / `## 환경` / `## 결과표` / `## 특이사항`
   - 요약에 PASS/FAIL/SKIP/전체 수치를 적는다.
2. `python3 .opencode/skills/test-report/scripts/validate.py output/test-report.md data/test_results.csv` 실행.
   - 검사: 필수 섹션의 본문, PASS+FAIL+SKIP=전체, CSV 원본과 요약·suite별 결과표 일치, 중복 테스트·미지원 상태·빈 셀·TODO/TBD.
   - "아마" 같은 불확실성 표현은 금지하지 않는다. 가설과 확인 사실은 구분한다.
3. FAIL → 지적 항목을 고치고 2를 다시 실행한다.
   **PASS가 나올 때까지 반복한다.** (최대 5회, 초과 시 보고)
4. PASS 출력 원문을 리포트 끝에 첨부한다.

## 금지
- 채점 없이 "완료" 보고 · 채점기 수정으로 통과 시도

## 폴더 구성
test-report/ ├─ SKILL.md └─ scripts/validate.py

## 판정 범위
PASS는 이 입력 CSV에 대한 형식·집계 대조 통과다. CSV 자체의 진실성, 환경 설명, 원인·해석의 정확성은 별도 검토한다. 검사기를 바꾸면 알려진 실패 사례의 회귀 테스트를 먼저 통과시킨다.
