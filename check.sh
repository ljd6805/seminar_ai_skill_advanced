#!/usr/bin/env bash
# SKILL QUEST 심화 시즌(시즌 2) 채점기 — 사용법: ./check.sh <mission-id>
# 통과 시 성장 코드(GROW-Lx-XXXX)를 출력합니다. 웹 보드에 입력하세요.
# (시즌 1(2편 Skill Quest)의 채점기와 같은 방식·같은 SALT — 레벨은 8~13)
set -u
SALT="skill-quest-2026-hbd"
ID="${1:-}"

pass() { # $1=level
  local code
  code=$(printf "%s%s" "$ID" "$SALT" | sha256sum | cut -c1-4 | tr 'a-f' 'A-F')
  echo ""
  echo "  ╔══════════════════════════════════╗"
  echo "  ║  ✔ MISSION CLEAR!                ║"
  echo "  ║  성장 코드: GROW-L$1-$code       ║"
  echo "  ╚══════════════════════════════════╝"
  echo "  웹 보드에 코드를 입력해 레벨업하세요."
  exit 0
}

fail() { echo ""; echo "  ✘ 아직입니다 — $1"; echo "  (막히면 에이전트에게 물어보는 것도 훌륭한 플레이입니다)"; exit 1; }

need_file() { [ -f "$1" ] || fail "$1 파일이 없습니다. 스킬이 발동되어 파일을 만들었는지 확인하세요."; }

ask() { # $1=question → y면 통과, 아니면 fail
  echo ""
  read -r -p "  $1 (y/n) " a
  [ "$a" = "y" ] || [ "$a" = "Y" ] || fail "직접 확인 후 다시 실행해주세요."
}

PY="$(command -v python || command -v python3 || true)"

case "$ID" in

  adv-script-offload)
    need_file output/digest.md
    for want in "FAIL_ASSERTION: 1842" "FAIL_TIMEOUT: 317" "FAIL_BUILD: 96" "FAIL_ENV: 41" "FIRST_SPIKE: 02:14"; do
      grep -qF "$want" output/digest.md \
        || fail "digest.md 의 수치가 스크립트 출력과 다릅니다 (기대: $want). 절차에 '그대로 옮겨 적는다'가 있나요? 에이전트가 직접 세기 시작했다면 ## 금지가 빠진 겁니다."
    done
    grep -qF "DIGEST-VERSION: 1" output/digest.md || fail "끝줄 DIGEST-VERSION: 1 이 없습니다. 형식은 본문에 못박는 것이었죠 (시즌 1 Lv.3)."
    grep -qF "GENERATED-BY: log-digest-skill" output/digest.md || fail "스킬 서명이 없습니다. 스킬이 정말 발동됐을까요? 재시작은 하셨나요?"
    [ -f .opencode/skills/log-digest/scripts/digest.py ] \
      || fail "digest.py 가 스킬 폴더(.opencode/skills/log-digest/scripts/)에 번들되어 있지 않습니다. 스크립트도 번들입니다 (시즌 1 Lv.5의 확장)."
    grep -qF "digest.py" .opencode/skills/log-digest/SKILL.md \
      || fail "SKILL.md 본문이 digest.py 실행을 지시하지 않습니다. 절차 교체를 확인하세요."
    grep -qF "직접 읽지 않는다" .opencode/skills/log-digest/SKILL.md \
      || fail "SKILL.md 에 '직접 읽지 않는다' 금지가 없습니다. 다음에 로그가 더 커져도 버티려면 금지까지 적어야 합니다."
    pass 8 ;;

  adv-artifact-contract)
    need_file output/digest.md
    for sec in "## 요약" "## 오류 Top 10" "## 이상 징후"; do
      grep -qF "$sec" output/digest.md \
        || fail "digest.md 에 '$sec' 섹션이 없습니다. 쓰는 쪽 약속(형식 3섹션)을 log-digest 본문에 적고 다시 발동시키세요."
    done
    grep -qF "DIGEST-VERSION: 1" output/digest.md || fail "digest.md 에 버전 표시가 없습니다. 약속은 경로·형식·버전 세 가지입니다."
    need_file output/report.md
    grep -qF "SOURCE: output/digest.md (DIGEST-VERSION: 1)" output/report.md \
      || fail "report.md 에 SOURCE 줄이 없습니다. 읽는 쪽이 '무엇을 근거로 썼는지'를 표기해야 전달이 추적됩니다."
    grep -qi "assertion" output/report.md \
      || fail "report.md 가 digest 의 원인 1위 유형을 인용하지 않았습니다. 리포트는 digest 만 근거로 써야 합니다."
    grep -qF "GENERATED-BY: incident-report-skill" output/report.md \
      || fail "리포트에 incident-report 서명이 없습니다. 스킬이 아니라 즉흥 답변이었을 수 있어요."
    grep -qF "멈춘다" .opencode/skills/incident-report/SKILL.md \
      || fail "incident-report 본문에 '없으면 멈춘다' 약속이 보이지 않습니다. 읽는 쪽 약속 3번을 확인하세요."
    echo "  [Lv.9 확인] 약속의 정지 조항을 실제로 시험했는지 확인합니다."
    ask "digest.md 가 없는 상태에서 리포트를 요청했을 때, 에이전트가 쓰지 않고 log-digest 실행을 안내하며 멈췄나요?"
    pass 9 ;;

  adv-pipeline)
    for f in output/digest.md output/analysis.md output/report.md output/verdict.md output/flow-log.md; do
      need_file "$f"
    done
    grep -qF "STEP 1/4" output/flow-log.md || fail "flow-log 에 STEP 1/4 기록이 없습니다. 첫 실행을 output/ 비운 상태에서 시작했나요?"
    grep -qF "GATE: FAIL" output/flow-log.md \
      || fail "flow-log 에 GATE: FAIL 기록이 없습니다. 반려를 겪는 것까지가 이 미션입니다 — root-cause 를 미리 고쳤다면 원복 후 처음부터(레시피 3번) 다시 진행하세요."
    grep -qF "SKIP 1/4" output/flow-log.md \
      || fail "flow-log 에 SKIP 1/4 기록이 없습니다. 보완 후 재실행 때 output/ 을 지우지 않아야 중간 재개(건너뜀)가 보입니다."
    grep -qF "GATE: PASS" output/flow-log.md || fail "flow-log 에 GATE: PASS 가 없습니다. 반려 사유(재현 절차)를 해소하고 재실행했나요?"
    grep -qF "STEP 4/4" output/flow-log.md || fail "flow-log 에 STEP 4/4 가 없습니다. 4단계(검증)까지 완주해야 합니다."
    grep -qF "## 재현 절차" output/analysis.md || fail "analysis.md 에 '## 재현 절차' 섹션이 없습니다."
    grep -q "TBD" output/analysis.md && fail "analysis.md 재현 절차에 TBD 가 남아 있습니다. root-cause 절차 4번 교체(레시피 5번)를 확인하세요."
    grep -qF "GENERATED-BY: report-check-skill" output/verdict.md \
      || fail "verdict.md 에 report-check 서명이 없습니다. 4단계가 스킬로 실행됐는지 확인하세요."
    [ -f .opencode/skills/incident-flow/SKILL.md ] || fail "incident-flow 스킬이 설치되어 있지 않습니다."
    grep -qF "## 금지" .opencode/skills/incident-flow/SKILL.md \
      || fail "incident-flow 에 ## 금지 절이 없습니다. 지휘 스킬의 금지(건너뛰기·순서 변경·빈손 완료)는 안전벨트입니다."
    [ -f .opencode/skills/incident-report/scripts/gate.py ] \
      || fail "gate.py 가 .opencode/skills/incident-report/scripts/ 에 없습니다. 게이트는 다음 단계의 입구에 섭니다."
    pass 10 ;;

  adv-validate-loop)
    VP=.opencode/skills/test-report/scripts/validate.py
    [ -f "$VP" ] || fail "validate.py 가 스킬 폴더($VP)에 없습니다. 뼈대를 복사해 빈칸을 채우세요."
    [ -n "$PY" ] || fail "python 을 찾을 수 없습니다. python 또는 python3 이 PATH 에 있어야 합니다."
    out=$("$PY" "$VP" scripts-given/fixtures/bad-report.md 2>&1); rc=$?
    echo "$out" | grep -q "채점기 미완성" && fail "validate.py 의 빈칸 1~3 이 아직 비어 있습니다."
    { [ "$rc" -ne 0 ] && echo "$out" | grep -qF "VALIDATE: FAIL"; } \
      || fail "여러분의 validate.py 가 불량 견본(scripts-given/fixtures/bad-report.md)을 통과시켰습니다. 채점기부터 채점에 합격해야죠 — 빈칸 1~3을 다시 보세요."
    need_file output/test-report-v3.md
    for want in "TOTAL: 19" "TOTAL_PASS: 12" "TOTAL_FAIL: 5" "TOTAL_SKIP: 2"; do
      grep -qF "$want" output/test-report-v3.md \
        || fail "리포트 수치가 CSV 정답과 다릅니다 (기대: $want). validate 의 지적문에 답이 적혀 있습니다 — 루프가 정말 PASS 까지 돌았나요?"
    done
    grep -qF "GRADE: RISK" output/test-report-v3.md \
      || fail "GRADE 판정이 없거나 기준서와 다릅니다. FAIL 5건을 기준표(references/quality-bar.md)에 대조해 보세요."
    grep -qF "REF-VERSION: QB-2026-07" output/test-report-v3.md || fail "REF-VERSION 이 없거나 틀렸습니다. 기준서 번들을 기억하세요 (시즌 1 Lv.5)."
    grep -qF "VALIDATE: PASS" output/test-report-v3.md \
      || fail "리포트에 VALIDATE: PASS 원문이 첨부되어 있지 않습니다. 증거를 남기는 것까지가 절차입니다."
    grep -qF "GENERATED-BY: test-report-skill" output/test-report-v3.md || fail "스킬 서명이 없습니다."
    grep -qF "5회" .opencode/skills/test-report/SKILL.md \
      || fail "SKILL.md 에 루프 상한(최대 5회)이 없습니다. 상한 없는 루프는 하네스가 아니라 도박입니다."
    "$PY" "$VP" output/test-report-v3.md >/dev/null 2>&1 \
      || fail "지금의 리포트가 여러분의 validate.py 를 통과하지 못합니다. 리포트를 고친 뒤 다시 오세요 — 판정은 코드가 합니다."
    pass 11 ;;

  adv-refute)
    need_file output/refute-log.md
    for want in "CLAIM:" "REFUTE-TIME:" "REFUTE-CASE:" "REFUTE-ALT:"; do
      grep -qF "$want" output/refute-log.md \
        || fail "refute-log 에 $want 기록이 없습니다. 3경로를 전부 시도해야 검증입니다 — 형식은 템플릿의 '형식 고정'을 따르세요."
    done
    grep -qF "VERDICT: REJECTED" output/refute-log.md \
      || fail "판정이 REJECTED 가 아닙니다. 시간 반박부터 다시 — 8/12 배포 '이전' 날짜의 로그를 정말 확인했나요?"
    grep -qiE "cert|인증서" output/refute-log.md \
      || fail "진짜 원인이 지목되지 않았습니다. 대안 반박에서 로그의 ERROR 메시지를 자세히 보세요 — 무엇이 만료됐나요?"
    grep -qF "GENERATED-BY: refute-check-skill" output/refute-log.md || fail "refute-check 서명이 없습니다."
    [ -f .opencode/skills/refute-check/SKILL.md ] || fail "refute-check 스킬이 설치되어 있지 않습니다."
    pass 12 ;;

  adv-final-weekly)
    need_file output/weekly-report.md
    grep -qF "SOURCE: output/digest.md (DIGEST-VERSION: 1)" output/weekly-report.md \
      || fail "SOURCE 줄이 없습니다. 리포트는 약속된 파일만 근거로 씁니다 (Lv.9)."
    grep -qF "GRADE: BLOCK" output/weekly-report.md \
      || fail "GRADE 가 없거나 기준서와 다릅니다. 이번 주 FAIL_TOTAL(digest 참조)을 기준표에 대조하면 몇 번째 줄일까요?"
    grep -qF "REF-VERSION: QB-2026-07" output/weekly-report.md || fail "REF-VERSION 이 없습니다. 기준서를 진짜로 읽었다는 증거가 필요합니다."
    grep -qF "## 증거표" output/weekly-report.md || fail "## 증거표 섹션이 없습니다. 증거가 없으면 완료가 아닙니다 (사건 ⑬)."
    rows=$(grep -c "^|" output/weekly-report.md || true)
    [ "${rows:-0}" -ge 5 ] || fail "증거표 행이 부족합니다 (현재 ${rows:-0}줄, 헤더 포함 5줄 이상). 실행한 점검을 행으로 남기세요 — 못 한 항목은 '미실행'으로."
    grep -qE '\| *(PASS|OK|미실행)' output/weekly-report.md \
      || fail "증거표에 판정 칸(PASS/OK/미실행)이 보이지 않습니다. 각 행은 명령·출력·판정을 담습니다."
    grep -qF "GENERATED-BY: regression-weekly-skill" output/weekly-report.md || fail "regression-weekly 서명이 없습니다."
    need_file output/digest.md
    grep -qF "FAIL_ASSERTION: 1842" output/digest.md || fail "digest.md 수치가 이번 주 데이터와 다릅니다. 1단계(집계)가 스크립트로 돌았는지 확인하세요."
    need_file output/analysis.md
    grep -q "TBD" output/analysis.md && fail "analysis.md 에 TBD 가 남아 있습니다. 게이트가 통과할 리 없죠 — 2단계를 보완하세요."
    ask "시작 후 완료 보고까지, 사람의 개입이 '주간 리그레션 리포트 만들어줘' 한 마디뿐이었나요?"
    pass 13 ;;

  adv-my-pipeline)
    echo ""
    echo "  EX 자율 퀘스트는 채점기가 없습니다 — 완성작을 웹 보드 도감에 등록하고 팀과 공유하면 클리어입니다."
    echo "  (미션 카드: missions/ex/adv-my-pipeline.md)"
    exit 0 ;;

  "")
    echo "사용법: ./check.sh <mission-id>"
    echo "심화 시즌 미션 목록:"
    ls missions/*/adv-*.md 2>/dev/null | sed 's|missions/[^/]*/||; s|\.md||; s|^|  - |' ;;

  *)
    fail "알 수 없는 미션 id 입니다: $ID (./check.sh 로 목록 확인)" ;;
esac
