---
name: test-report
description: 테스트 결과 집계·주간 리포트 작성 시 사용 (기계 채점 포함)
---
# Test Report

## 절차
1. `data/test_results.csv` 를 집계해 리포트를 `output/test-report.md` 로 작성한다.
   - 필수 섹션: `## 요약` / `## 환경` / `## 결과표` / `## 특이사항`
   - 요약에 PASS/FAIL/SKIP/전체 수치를 적는다.
2. `python3 .opencode/skills/test-report/scripts/validate.py output/test-report.md` 실행.
   - 검사: 필수 섹션 존재 · PASS+FAIL+SKIP=전체 합계 · 금지 문구("아마" 등)·빈 셀 없음
3. FAIL → 지적 항목을 고치고 2를 다시 실행한다.
   **PASS가 나올 때까지 반복한다.** (최대 5회, 초과 시 보고)
4. PASS 출력 원문을 리포트 끝에 첨부한다.

## 금지
- 채점 없이 "완료" 보고 · 채점기 수정으로 통과 시도

## 폴더 구성
test-report/ ├─ SKILL.md └─ scripts/validate.py
