#!/usr/bin/env python3
"""로그 집계기 — 원본은 컨텍스트 밖에서 코드가 훑고, 결과 요약만 돌려준다.

사용: python3 digest.py <로그경로>
출력: 유형별 건수 · 첫 발생 시각 · 첫 급증 시각 · 대표 사례 · TOTAL (약 30줄)
"""
import re
import sys
from collections import Counter, OrderedDict

LINE = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}):\d{2}\.\d+ (\w+) \[([^\]]+)\] (.*)$")
ERR = re.compile(r"\b([A-Z][A-Za-z]*(?:Error|Exception|Timeout))\b")


def main(path: str) -> None:
    counts: Counter = Counter()
    first_seen: "OrderedDict[str, str]" = OrderedDict()
    sample: dict = {}
    per_minute: Counter = Counter()
    total_lines = 0

    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            total_lines += 1
            m = LINE.match(line)
            if not m or m.group(3) != "ERROR":
                continue
            minute = m.group(2)
            e = ERR.search(m.group(5))
            etype = e.group(1) if e else "UnknownError"
            counts[etype] += 1
            per_minute[minute] += 1
            first_seen.setdefault(etype, minute)
            sample.setdefault(etype, m.group(5)[:110])

    total_err = sum(counts.values())
    print(f"== LOG DIGEST: {path} ==")
    print(f"스캔한 줄 수     : {total_lines:,}")
    print(f"TOTAL ERRORS     : {total_err:,}")
    print()
    print("-- 유형별 건수 (많은 순) --")
    for etype, n in counts.most_common():
        print(f"{etype:<24} {n:>7,}건   첫 발생 {first_seen[etype]}")
    print()
    nonzero = sorted(per_minute.values())
    if nonzero:
        median = nonzero[len(nonzero) // 2]
        threshold = max(10, median * 5)
        surge = next(
            (mn for mn, n in sorted(per_minute.items()) if n >= threshold), None
        )
        peak_min, peak_n = max(per_minute.items(), key=lambda kv: kv[1])
        print(f"첫 급증 시각     : {surge or '없음'} (기준: 분당 {threshold}건 이상)")
        print(f"최다 발생 분     : {peak_min} ({peak_n:,}건)")
    print()
    print("-- 유형별 대표 사례 (상위 5) --")
    for etype, _ in counts.most_common(5):
        print(f"{etype}: {sample[etype]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("사용법: python3 digest.py <로그경로>")
    main(sys.argv[1])
