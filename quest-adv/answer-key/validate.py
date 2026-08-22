#!/usr/bin/env python
# Lv.11 validate.py 완성본 (진행자용 답안) — 뼈대와 동일하되 빈칸 3곳이 채워져 있음
import re
import sys

REQUIRED_SECTIONS = ["## 요약", "## 판정"]
BANNED_WORDS = ["TODO", "TBD", "대략"]


def counts_match(report_value, truth_value):
    return report_value == truth_value


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
