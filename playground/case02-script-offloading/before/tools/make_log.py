#!/usr/bin/env python3
"""체험용 리그레션 로그 생성기 — logs/regression.log 를 만든다.

기본 500,000줄 (~45MB). 심어 둔 정답(슬라이드와 동일):
  AssertionError 1,842건 · TimeoutError 317건 · 첫 급증 02:14
빠른 체험: python3 tools/make_log.py --lines 50000
"""
import argparse
import os
import random

SUITES = ["checkout", "cart", "auth", "search", "shipping", "coupon", "refund"]
INFO = [
    "case started", "fixture loaded", "request ok (200)", "warm cache hit",
    "snapshot compared", "retry scheduled", "case finished", "teardown done",
]
PLANT = [  # (오류 유형, 총 건수, 급증 여부)
    ("AssertionError", 1842, True),
    ("TimeoutError", 317, False),
    ("ConnectionResetError", 96, False),
]
SURGE_START = 134  # 02:14 (00:00 기준 경과 분)
SURGE_END = 210    # 03:30


def stamp(minute: int, rnd: random.Random) -> str:
    return f"2026-08-24 {minute // 60:02d}:{minute % 60:02d}:{rnd.randrange(60):02d}.{rnd.randrange(1000):03d}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", type=int, default=500_000, help="총 줄 수 (기본 500,000)")
    ap.add_argument("--out", default="logs/regression.log")
    args = ap.parse_args()
    if args.lines < 5_000:
        raise SystemExit("--lines 는 5,000 이상이어야 심은 정답이 유지됩니다.")

    rnd = random.Random(42)
    rows = []
    for etype, n, surge in PLANT:
        for i in range(n):
            if surge and i >= n * 0.05:  # 5%만 급증 전, 나머지는 02:14~03:30 폭증
                minute = rnd.randrange(SURGE_START, SURGE_END)
            else:
                minute = rnd.randrange(0, 360)
            suite = rnd.choice(SUITES)
            msg = {
                "AssertionError": f"AssertionError: expected total=18400 got={rnd.randrange(15000, 18400)} (case tc_{rnd.randrange(1000):04d})",
                "TimeoutError": f"TimeoutError: no response in 30s from stage-api (case tc_{rnd.randrange(1000):04d})",
                "ConnectionResetError": "ConnectionResetError: [Errno 104] peer closed during fixture setup",
            }[etype]
            rows.append((minute, f"ERROR [suite.{suite}] {msg}"))

    info_n = args.lines - len(rows)
    for _ in range(info_n):
        minute = rnd.randrange(0, 360)
        rows.append((minute, f"INFO [suite.{rnd.choice(SUITES)}] {rnd.choice(INFO)} (case tc_{rnd.randrange(1000):04d})"))

    rows.sort(key=lambda r: r[0])
    out_dir = os.path.dirname(args.out)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        for minute, body in rows:
            f.write(f"{stamp(minute, rnd)} {body}\n")
    print(f"{args.out}: {len(rows):,}줄 생성 (AssertionError 1,842 · TimeoutError 317 · 첫 급증 02:14)")


if __name__ == "__main__":
    main()
