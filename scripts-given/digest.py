#!/usr/bin/env python
# log-digest 스킬 동봉용 집계 스크립트 (Lv.8 제공물)
# 사용법: python .opencode/skills/log-digest/scripts/digest.py <로그경로>
# 컨텍스트 밖에서 전체 로그를 훑어, 모델이 옮겨 적을 결과 몇 줄만 출력합니다.
import sys
from collections import Counter


def classify(line):
    if "UVM_ERROR" in line:
        return "ASSERTION"
    if "TIMEOUT" in line:
        return "TIMEOUT"
    if "BUILD ERROR" in line:
        return "BUILD"
    if "ENV ERROR" in line:
        return "ENV"
    return None


def main():
    if len(sys.argv) < 2:
        print("사용법: python digest.py <로그경로>")
        sys.exit(2)
    path = sys.argv[1]

    total = 0
    buckets = Counter()
    stacks = Counter()
    per_minute = Counter()
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                total += 1
                typ = classify(line)
                if typ:
                    buckets[typ] += 1
                    # 시그니처: FAIL 뒤의 오류 본문
                    sig = line.split("FAIL", 1)[-1].strip() if "FAIL" in line else line.strip()
                    stacks[sig] += 1
                    # [YYYY-mm-dd HH:MM:SS] → HH:MM
                    if line.startswith("[") and len(line) > 18:
                        per_minute[line[12:17]] += 1
    except FileNotFoundError:
        print(f"FAIL: 로그 파일이 없습니다 — {path}")
        sys.exit(2)

    spike = per_minute.most_common(1)[0][0] if per_minute else "-"

    print("== LOG DIGEST (scripts/digest.py) ==")
    print(f"TOTAL_LINES: {total}")
    print(f"FAIL_ASSERTION: {buckets['ASSERTION']}")
    print(f"FAIL_TIMEOUT: {buckets['TIMEOUT']}")
    print(f"FAIL_BUILD: {buckets['BUILD']}")
    print(f"FAIL_ENV: {buckets['ENV']}")
    print(f"FAIL_TOTAL: {sum(buckets.values())}")
    print(f"FIRST_SPIKE: {spike}")
    print("== TOP STACKS (상위 20) ==")
    for sig, cnt in stacks.most_common(20):
        print(f"  {cnt:>5}x  {sig}")


if __name__ == "__main__":
    main()
