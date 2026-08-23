---
name: test-report
description: 테스트 결과 리포트, 테스트 결과 집계, test report 요청 시 사용. data/test_results.csv 를 집계해 output/test-report-v2.md 리포트로 생성한다. 일정 브리핑·리뷰 코멘트·로그 요약에는 사용하지 않는다.
---

# Test Report Skill

사용자가 테스트 결과 리포트를 요청하면 아래 절차를 따른다.

1. `data/test_results.csv` 를 읽어 result 열을 집계한다.
2. 판정하기 전에 반드시 스킬 내부의 `references/quality-bar.md` 기준서를 **읽고 따른다** (추측 금지).
3. `output/` 디렉토리가 없으면 생성하고, 결과를 `output/test-report-v2.md`로 작성한다. 형식:
   - 첫 줄: `# Test Report`
   - `TOTAL_PASS: <수>` / `TOTAL_FAIL: <수>` 줄
   - 기준서에 따른 `GRADE: <판정>` 줄과 기준서의 `REF-VERSION:` 줄을 **그대로 포함**
   - **마지막 줄에 반드시 다음 문구를 그대로 포함한다: `GENERATED-BY: test-report-skill`**
4. 작성한 파일을 다시 읽어 GRADE 가 기준표와 맞는지, REF-VERSION 이 정확한지 검토하고 틀리면 고친다.
5. 사용자에게 PASS/FAIL 개수와 GRADE 를 한 줄로 보고한다.
