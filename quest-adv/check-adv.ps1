param([string]$Id = "")
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}
$SALT = "skill-quest-2026-hbd"

function Get-GrowthCode([string]$mid) {
  $sha = [System.Security.Cryptography.SHA256]::Create()
  $hash = $sha.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($mid + $SALT))
  $hex = ($hash | ForEach-Object { $_.ToString("x2") }) -join ""
  return $hex.Substring(0,4).ToUpper()
}

function Pass([int]$Lvl) {
  $code = Get-GrowthCode $Id
  Write-Host ""
  Write-Host "  ======================================"
  Write-Host "    [V] MISSION CLEAR!"
  Write-Host "    성장 코드: GROW-L$Lvl-$code"
  Write-Host "  ======================================"
  Write-Host "  웹 보드에 코드를 입력해 레벨업하세요."
  exit 0
}

function Fail([string]$Msg) {
  Write-Host ""
  Write-Host "  [X] 아직입니다 - $Msg"
  Write-Host "  (막히면 에이전트에게 물어보는 것도 훌륭한 플레이입니다)"
  exit 1
}

function Need-File([string]$Path) {
  if (-not (Test-Path $Path)) { Fail "$Path 파일이 없습니다. 스킬이 발동되어 파일을 만들었는지 확인하세요." }
}

function Ask([string]$Q) {
  $a = Read-Host "  $Q (y/n)"
  if ($a -ne "y" -and $a -ne "Y") { Fail "직접 확인 후 다시 실행해주세요." }
}

function HasF([string]$File, [string]$Text) {   # 문자열 그대로 (SimpleMatch)
  return [bool](Select-String -Path $File -SimpleMatch $Text -Quiet)
}
function HasR([string]$File, [string]$Pattern) { # 정규식
  return [bool](Select-String -Path $File -Pattern $Pattern -Quiet)
}

if ($Id -eq "") {
  Write-Host "SKILL QUEST 심화 시즌 채점기 - 미션 목록:"
  Get-ChildItem -Path "missions" -Recurse -Filter "adv-*.md" | ForEach-Object { Write-Host ("  - " + $_.BaseName) }
  Write-Host "  (기초 시즌 미션은 check.bat 로 채점합니다)"
  $Id = (Read-Host "채점할 미션 id 를 입력하세요").Trim()
  if ($Id -eq "") { Fail "미션 id 가 입력되지 않았습니다." }
}

switch ($Id) {

  "adv-script-offload" {
    Need-File "output/digest.md"
    foreach ($want in @("FAIL_ASSERTION: 1842","FAIL_TIMEOUT: 317","FAIL_BUILD: 96","FAIL_ENV: 41","FIRST_SPIKE: 02:14")) {
      if (-not (HasF "output/digest.md" $want)) {
        Fail "digest.md 의 수치가 스크립트 출력과 다릅니다 (기대: $want). 절차에 '그대로 옮겨 적는다'가 있나요? 에이전트가 직접 세기 시작했다면 ## 금지가 빠진 겁니다." } }
    if (-not (HasF "output/digest.md" "DIGEST-VERSION: 1")) { Fail "끝줄 DIGEST-VERSION: 1 이 없습니다. 형식은 본문에 못박는 것이었죠 (시즌 1 Lv.3)." }
    if (-not (HasF "output/digest.md" "GENERATED-BY: log-digest-skill")) { Fail "스킬 서명이 없습니다. 스킬이 정말 발동됐을까요? 재시작은 하셨나요?" }
    if (-not (Test-Path ".opencode/skills/log-digest/scripts/digest.py")) {
      Fail "digest.py 가 스킬 폴더(.opencode/skills/log-digest/scripts/)에 번들되어 있지 않습니다. 스크립트도 번들입니다 (시즌 1 Lv.5의 확장)." }
    if (-not (HasF ".opencode/skills/log-digest/SKILL.md" "digest.py")) { Fail "SKILL.md 본문이 digest.py 실행을 지시하지 않습니다. 절차 교체를 확인하세요." }
    if (-not (HasF ".opencode/skills/log-digest/SKILL.md" "직접 읽지 않는다")) { Fail "SKILL.md 에 '직접 읽지 않는다' 금지가 없습니다. 다음에 로그가 더 커져도 버티려면 금지까지 적어야 합니다." }
    Pass 8 }

  "adv-artifact-contract" {
    Need-File "output/digest.md"
    foreach ($sec in @("## 요약","## 오류 Top 10","## 이상 징후")) {
      if (-not (HasF "output/digest.md" $sec)) { Fail "digest.md 에 '$sec' 섹션이 없습니다. 쓰는 쪽 약속(형식 3섹션)을 log-digest 본문에 적고 다시 발동시키세요." } }
    if (-not (HasF "output/digest.md" "DIGEST-VERSION: 1")) { Fail "digest.md 에 버전 표시가 없습니다. 약속은 경로·형식·버전 세 가지입니다." }
    Need-File "output/report.md"
    if (-not (HasF "output/report.md" "SOURCE: output/digest.md (DIGEST-VERSION: 1)")) {
      Fail "report.md 에 SOURCE 줄이 없습니다. 읽는 쪽이 '무엇을 근거로 썼는지'를 표기해야 전달이 추적됩니다." }
    if (-not (HasR "output/report.md" "(?i)assertion")) { Fail "report.md 가 digest 의 원인 1위 유형을 인용하지 않았습니다. 리포트는 digest 만 근거로 써야 합니다." }
    if (-not (HasF "output/report.md" "GENERATED-BY: incident-report-skill")) { Fail "리포트에 incident-report 서명이 없습니다. 스킬이 아니라 즉흥 답변이었을 수 있어요." }
    if (-not (HasF ".opencode/skills/incident-report/SKILL.md" "멈춘다")) { Fail "incident-report 본문에 '없으면 멈춘다' 약속이 보이지 않습니다. 읽는 쪽 약속 3번을 확인하세요." }
    Write-Host "  [Lv.9 확인] 약속의 정지 조항을 실제로 시험했는지 확인합니다."
    Ask "digest.md 가 없는 상태에서 리포트를 요청했을 때, 에이전트가 쓰지 않고 log-digest 실행을 안내하며 멈췄나요?"
    Pass 9 }

  "adv-pipeline" {
    foreach ($f in @("output/digest.md","output/analysis.md","output/report.md","output/verdict.md","output/flow-log.md")) { Need-File $f }
    if (-not (HasF "output/flow-log.md" "STEP 1/4")) { Fail "flow-log 에 STEP 1/4 기록이 없습니다. 첫 실행을 output/ 비운 상태에서 시작했나요?" }
    if (-not (HasF "output/flow-log.md" "GATE: FAIL")) { Fail "flow-log 에 GATE: FAIL 기록이 없습니다. 반려를 겪는 것까지가 이 미션입니다 - root-cause 를 미리 고쳤다면 원복 후 처음부터(레시피 3번) 다시 진행하세요." }
    if (-not (HasF "output/flow-log.md" "SKIP 1/4")) { Fail "flow-log 에 SKIP 1/4 기록이 없습니다. 보완 후 재실행 때 output/ 을 지우지 않아야 중간 재개(건너뜀)가 보입니다." }
    if (-not (HasF "output/flow-log.md" "GATE: PASS")) { Fail "flow-log 에 GATE: PASS 가 없습니다. 반려 사유(재현 절차)를 해소하고 재실행했나요?" }
    if (-not (HasF "output/flow-log.md" "STEP 4/4")) { Fail "flow-log 에 STEP 4/4 가 없습니다. 4단계(검증)까지 완주해야 합니다." }
    if (-not (HasF "output/analysis.md" "## 재현 절차")) { Fail "analysis.md 에 '## 재현 절차' 섹션이 없습니다." }
    if (HasF "output/analysis.md" "TBD") { Fail "analysis.md 재현 절차에 TBD 가 남아 있습니다. root-cause 절차 4번 교체(레시피 5번)를 확인하세요." }
    if (-not (HasF "output/verdict.md" "GENERATED-BY: report-check-skill")) { Fail "verdict.md 에 report-check 서명이 없습니다. 4단계가 스킬로 실행됐는지 확인하세요." }
    if (-not (Test-Path ".opencode/skills/incident-flow/SKILL.md")) { Fail "incident-flow 스킬이 설치되어 있지 않습니다." }
    if (-not (HasF ".opencode/skills/incident-flow/SKILL.md" "## 금지")) { Fail "incident-flow 에 ## 금지 절이 없습니다. 지휘 스킬의 금지(건너뛰기·순서 변경·빈손 완료)는 안전벨트입니다." }
    if (-not (Test-Path ".opencode/skills/incident-report/scripts/gate.py")) { Fail "gate.py 가 .opencode/skills/incident-report/scripts/ 에 없습니다. 게이트는 다음 단계의 입구에 섭니다." }
    Pass 10 }

  "adv-validate-loop" {
    $vp = ".opencode/skills/test-report/scripts/validate.py"
    if (-not (Test-Path $vp)) { Fail "validate.py 가 스킬 폴더($vp)에 없습니다. 뼈대를 복사해 빈칸을 채우세요." }
    $out = (& python $vp "scripts-given/fixtures/bad-report.md" 2>&1 | Out-String); $rc = $LASTEXITCODE
    if ($out -match "채점기 미완성") { Fail "validate.py 의 빈칸 1~3 이 아직 비어 있습니다." }
    if ($rc -eq 0 -or ($out -notmatch "VALIDATE: FAIL")) {
      Fail "여러분의 validate.py 가 불량 견본(scripts-given/fixtures/bad-report.md)을 통과시켰습니다. 채점기부터 채점에 합격해야죠 - 빈칸 1~3을 다시 보세요." }
    Need-File "output/test-report-v3.md"
    foreach ($want in @("TOTAL: 19","TOTAL_PASS: 12","TOTAL_FAIL: 5","TOTAL_SKIP: 2")) {
      if (-not (HasF "output/test-report-v3.md" $want)) {
        Fail "리포트 수치가 CSV 정답과 다릅니다 (기대: $want). validate 의 지적문에 답이 적혀 있습니다 - 루프가 정말 PASS 까지 돌았나요?" } }
    if (-not (HasF "output/test-report-v3.md" "GRADE: RISK")) { Fail "GRADE 판정이 없거나 기준서와 다릅니다. FAIL 5건을 기준표(references/quality-bar.md)에 대조해 보세요." }
    if (-not (HasF "output/test-report-v3.md" "REF-VERSION: QB-2026-07")) { Fail "REF-VERSION 이 없거나 틀렸습니다. 기준서 번들을 기억하세요 (시즌 1 Lv.5)." }
    if (-not (HasF "output/test-report-v3.md" "VALIDATE: PASS")) { Fail "리포트에 VALIDATE: PASS 원문이 첨부되어 있지 않습니다. 증거를 남기는 것까지가 절차입니다." }
    if (-not (HasF "output/test-report-v3.md" "GENERATED-BY: test-report-skill")) { Fail "스킬 서명이 없습니다." }
    if (-not (HasF ".opencode/skills/test-report/SKILL.md" "5회")) { Fail "SKILL.md 에 루프 상한(최대 5회)이 없습니다. 상한 없는 루프는 하네스가 아니라 도박입니다." }
    & python $vp "output/test-report-v3.md" *> $null
    if ($LASTEXITCODE -ne 0) { Fail "지금의 리포트가 여러분의 validate.py 를 통과하지 못합니다. 리포트를 고친 뒤 다시 오세요 - 판정은 코드가 합니다." }
    Pass 11 }

  "adv-refute" {
    Need-File "output/refute-log.md"
    foreach ($want in @("CLAIM:","REFUTE-TIME:","REFUTE-CASE:","REFUTE-ALT:")) {
      if (-not (HasF "output/refute-log.md" $want)) { Fail "refute-log 에 $want 기록이 없습니다. 3경로를 전부 시도해야 검증입니다 - 형식은 템플릿의 '형식 고정'을 따르세요." } }
    if (-not (HasF "output/refute-log.md" "VERDICT: REJECTED")) { Fail "판정이 REJECTED 가 아닙니다. 시간 반박부터 다시 - 8/12 배포 '이전' 날짜의 로그를 정말 확인했나요?" }
    if (-not (HasR "output/refute-log.md" "(?i)cert|인증서")) { Fail "진짜 원인이 지목되지 않았습니다. 대안 반박에서 로그의 ERROR 메시지를 자세히 보세요 - 무엇이 만료됐나요?" }
    if (-not (HasF "output/refute-log.md" "GENERATED-BY: refute-check-skill")) { Fail "refute-check 서명이 없습니다." }
    if (-not (Test-Path ".opencode/skills/refute-check/SKILL.md")) { Fail "refute-check 스킬이 설치되어 있지 않습니다." }
    Pass 12 }

  "adv-final-weekly" {
    Need-File "output/weekly-report.md"
    if (-not (HasF "output/weekly-report.md" "SOURCE: output/digest.md (DIGEST-VERSION: 1)")) { Fail "SOURCE 줄이 없습니다. 리포트는 약속된 파일만 근거로 씁니다 (Lv.9)." }
    if (-not (HasF "output/weekly-report.md" "GRADE: BLOCK")) { Fail "GRADE 가 없거나 기준서와 다릅니다. 이번 주 FAIL_TOTAL(digest 참조)을 기준표에 대조하면 몇 번째 줄일까요?" }
    if (-not (HasF "output/weekly-report.md" "REF-VERSION: QB-2026-07")) { Fail "REF-VERSION 이 없습니다. 기준서를 진짜로 읽었다는 증거가 필요합니다." }
    if (-not (HasF "output/weekly-report.md" "## 증거표")) { Fail "## 증거표 섹션이 없습니다. 증거가 없으면 완료가 아닙니다 (사건 13)." }
    $rows = (Select-String -Path "output/weekly-report.md" -Pattern "^\|" | Measure-Object).Count
    if ($rows -lt 5) { Fail "증거표 행이 부족합니다 (현재 $rows 줄, 헤더 포함 5줄 이상). 실행한 점검을 행으로 남기세요 - 못 한 항목은 '미실행'으로." }
    if (-not (HasR "output/weekly-report.md" "\| *(PASS|OK|미실행)")) { Fail "증거표에 판정 칸(PASS/OK/미실행)이 보이지 않습니다. 각 행은 명령·출력·판정을 담습니다." }
    if (-not (HasF "output/weekly-report.md" "GENERATED-BY: regression-weekly-skill")) { Fail "regression-weekly 서명이 없습니다." }
    Need-File "output/digest.md"
    if (-not (HasF "output/digest.md" "FAIL_ASSERTION: 1842")) { Fail "digest.md 수치가 이번 주 데이터와 다릅니다. 1단계(집계)가 스크립트로 돌았는지 확인하세요." }
    Need-File "output/analysis.md"
    if (HasF "output/analysis.md" "TBD") { Fail "analysis.md 에 TBD 가 남아 있습니다. 게이트가 통과할 리 없죠 - 2단계를 보완하세요." }
    Ask "시작 후 완료 보고까지, 사람의 개입이 '주간 리그레션 리포트 만들어줘' 한 마디뿐이었나요?"
    Pass 13 }

  "adv-my-pipeline" {
    Write-Host ""
    Write-Host "  EX 자율 퀘스트는 채점기가 없습니다 - 완성작을 웹 보드 도감에 등록하고 팀과 공유하면 클리어입니다."
    Write-Host "  (미션 카드: missions/ex/adv-my-pipeline.md)"
    exit 0 }

  default { Fail "알 수 없는 미션 id 입니다: $Id (인자 없이 실행하면 목록이 표시됩니다 - 기초 시즌은 check.bat)" }
}
