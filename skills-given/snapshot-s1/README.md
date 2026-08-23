# 시즌 1 세이브 파일 (snapshot-s1) — 심화 시즌의 공통 출발점

시즌 1(2편 [Skill Quest](https://github.com/ljd6805/seminar_ai_skill_quest))을 완주한 상태의 스킬 4종입니다.
심화 시즌은 이 리포 하나로 독립 진행되므로, **모든 참가자가 이 폴더를 설치하고 시작**합니다 —
2편 수료 여부나 그때의 리포 보유 여부와 무관하게 출발선이 같습니다.

설치 (Lv.8 미션 카드의 "공통 준비"와 동일):

- Linux: `mkdir -p .opencode/skills && cp -r skills-given/snapshot-s1/daily-report skills-given/snapshot-s1/log-digest skills-given/snapshot-s1/test-report skills-given/snapshot-s1/review-summary .opencode/skills/`
- Windows(PowerShell): `New-Item -Type Directory -Force .opencode\skills | Out-Null; Copy-Item -Recurse skills-given\snapshot-s1\daily-report,skills-given\snapshot-s1\log-digest,skills-given\snapshot-s1\test-report,skills-given\snapshot-s1\review-summary .opencode\skills\`
- 복사 후 opencode 재시작을 잊지 마세요.

구성: daily-report(Lv.1 제공 스킬) · log-digest(Lv.2 수리 완료) · test-report(Lv.3~5 제작+방어선+기준서 번들) · review-summary(Lv.6 승급 시험 통과).
시즌 1을 직접 완주했던 분에게는 복습 자료이기도 합니다 — 각 SKILL.md가 그때 배운 다섯 재료의 실물입니다.
