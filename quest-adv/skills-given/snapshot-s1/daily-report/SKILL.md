---
name: daily-report
description: 오늘 일정 요약, 일일 브리핑, 오늘 작업 요약, daily report 요청 시 사용. data/schedule/today.md 의 일정을 조회해 output/daily-report.md 리포트로 생성한다.
---

# Daily Report Skill

사용자가 오늘 일정 브리핑이나 일일 리포트를 요청하면 아래 절차를 따른다.

1. `data/schedule/today.md` 파일 **하나만** 읽는다. 이 파일이 유일한 정보원이다.
   - **금지 사항**: git 명령 실행, 커밋·브랜치·수정 파일 조회, 디렉토리 탐색, 그 외 다른 파일 읽기.
   - 리포트에 git/커밋/staging 관련 내용이 한 줄이라도 들어가면 실패로 간주한다.
2. `output/` 디렉토리가 없으면 생성한다.
3. 일정을 시간순으로 3~5개의 불릿으로 요약해 `output/daily-report.md` 파일로 작성한다. 형식:
   - 첫 줄: `# Daily Report`
   - 일정 요약 불릿들
   - **마지막 줄에 반드시 다음 문구를 그대로 포함한다: `GENERATED-BY: daily-report-skill`**
4. 파일을 만든 뒤 사용자에게 한 줄로 완료를 알린다.
