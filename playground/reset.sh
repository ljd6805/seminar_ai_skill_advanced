#!/usr/bin/env bash
# playground 를 체험 전 상태로 되돌린다.
#  1) gitignore 대상 생성물(대용량 로그, output/*.md 산출물 등) 삭제
#  2) 체험 중 수정된 '추적 파일' 원복 — ⚠ 커밋하지 않은 수정도 함께 되돌린다
# 확인 없이 실행: bash reset.sh --yes
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"

if [ "${1:-}" != "--yes" ]; then
  echo "[reset] 원복될 추적 파일 변경 목록:"
  git -C "$REPO" status --short -- playground || true
  printf "[reset] 위 변경을 모두 되돌리고 생성물을 지웁니다. 계속할까요? [y/N] "
  read -r ans
  case "$ans" in y|Y) ;; *) echo "[reset] 취소"; exit 1 ;; esac
fi

git -C "$REPO" clean -fdX -- playground
git -C "$REPO" checkout -- playground
echo "[reset] 완료 — 생성물 삭제 + 추적 파일 원복."
