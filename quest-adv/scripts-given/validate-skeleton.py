#!/usr/bin/env python
# test-report 스킬 동봉용 채점기 뼈대 (Lv.11)
# 여러분이 채울 곳은 [빈칸 1] [빈칸 2] [빈칸 3] 세 곳뿐입니다. 나머지는 완성되어 있습니다.
#
# 설치:  .opencode/skills/test-report/scripts/validate.py 로 복사해 빈칸을 채우세요.
# 사용법: python .opencode/skills/test-report/scripts/validate.py output/test-report-v3.md
#         (두 번째 인자로 CSV 경로를 줄 수 있으며, 기본값은 data/test_results_week34.csv)
import re
import sys

# ── [빈칸 1] 리포트에 반드시 있어야 하는 섹션 제목 2개를 채우세요 ─────────────
#    예: ["## 요약", "## 판정"]
REQUIRED_SECTIONS = []

# ── [빈칸 2] 리포트에 있으면 안 되는 애매한 표현들을 채우세요 ────────────────
#    예: ["TODO", "TBD", "대략"]   (수치는 정확한 값만 — 추정 금지)
BANNED_WORDS = []


def counts_match(report_value, truth_value):
    # ── [빈칸 3] 리포트 수치와 CSV 정답이 '일치'하는 조건을 return 하세요 ────
    #    한 줄이면 됩니다.
    return False


# ───────────────────── 아래부터는 완성된 부분 (수정 불필요) ─────────────────────

def truth_from_csv(csv_path):
    """CSV에서 정답을 다시 센다 — 같은 테스트가 여러 번이면 마지막 결과만 인정."""
    last = {}
    with open(csv_path, encoding="utf-8") as f:
        header = f.readline()
        for row in f:
            cols = [c.strip() for c in row.split(",")]
            if len(cols) < 3:
                continue
            last[cols[0]] = cols[2].upper()
    truth = {"TOTAL_PASS": 0, "TOTAL_FAIL": 0, "TOTAL_SKIP": 0}
    for result in last.values():
        key = f"TOTAL_{result}"
        if key in truth:
            truth[key] += 1
    truth["TOTAL"] = len(last)
    return truth


def report_numbers(text):
    nums = {}
    for key in ["TOTAL_PASS", "TOTAL_FAIL", "TOTAL_SKIP", "TOTAL"]:
        m = re.search(rf"^{key}:\s*(\d+)\s*$", text, re.MULTILINE)
        nums[key] = int(m.group(1)) if m else None
    return nums


def main():
    if not REQUIRED_SECTIONS or not BANNED_WORDS:
        print("VALIDATE: FAIL (채점기 미완성)")
        print("  - validate.py 의 [빈칸 1]~[빈칸 3] 을 먼저 채우세요")
        sys.exit(2)

    report_path = sys.argv[1] if len(sys.argv) > 1 else "output/test-report-v3.md"
    csv_path = sys.argv[2] if len(sys.argv) > 2 else "data/test_results_week34.csv"
    try:
        text = open(report_path, encoding="utf-8").read()
    except FileNotFoundError:
        print("VALIDATE: FAIL")
        print(f"  - 리포트 파일이 없습니다: {report_path}")
        sys.exit(1)

    truth = truth_from_csv(csv_path)
    nums = report_numbers(text)
    problems = []

    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            problems.append(f"필수 섹션 '{sec}' 이 없습니다")

    for key in ["TOTAL_PASS", "TOTAL_FAIL", "TOTAL_SKIP", "TOTAL"]:
        if nums[key] is None:
            hint = " — CSV의 result 열에는 SKIP 도 있습니다" if key == "TOTAL_SKIP" else ""
            problems.append(f"{key}: 줄이 없습니다{hint}")
        elif not counts_match(nums[key], truth[key]):
            problems.append(
                f"{key}: 리포트 {nums[key]} ≠ CSV 정답 {truth[key]}"
                " — 같은 테스트가 두 번 실행됐다면 마지막 결과만 셉니다"
            )

    if None not in nums.values():
        s = nums["TOTAL_PASS"] + nums["TOTAL_FAIL"] + nums["TOTAL_SKIP"]
        if s != nums["TOTAL"]:
            problems.append(f"합계 불일치: PASS+FAIL+SKIP={s} 인데 TOTAL={nums['TOTAL']}")

    for word in BANNED_WORDS:
        if word in text:
            problems.append(f"금지 문구 '{word.strip()}' 발견 — 수치는 정확한 값만 적으세요")

    if problems:
        print(f"VALIDATE: FAIL (지적 {len(problems)}건)")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)

    print("VALIDATE: PASS")
    print(f"  checked: sections({len(REQUIRED_SECTIONS)}) counts(4) banned(0 hit)")
    print(f"  source : {csv_path} (unique tests: {truth['TOTAL']})")
    sys.exit(0)


if __name__ == "__main__":
    main()
