#!/usr/bin/env bash
# playground 체험 중 생성된 산출물을 지워 초기 상태로 되돌린다.
# (git 으로 추적되는 SKILL.md·샘플·정답 파일은 건드리지 않는다.)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

echo "[reset] ② 생성된 대용량 로그 삭제"
rm -rf case02-script-offloading/*/logs

echo "[reset] ③ 재개 실험으로 변경된 state.md 를 원위치(03에서 끊긴 상태)로"
# after/output/state.md 는 git 추적본. 체험 중 바뀌었으면 checkout 으로 복구.
git -C "$HERE/.." checkout -- playground/case03-external-memory/after/output/state.md 2>/dev/null || true

echo "[reset] ⑥⑦ 파이프라인 산출물(output/*.md) 삭제 — 단, 추적되는 샘플은 보존"
find case06-artifact-contract case07-pipeline -type d -name output -exec rm -rf {} + 2>/dev/null || true

echo "[reset] ⑩ 자가 리뷰 초안 산출물 삭제"
rm -rf case10-self-review/*/output

echo "[reset] 완료. (git status 로 남은 변경을 확인하세요)"
