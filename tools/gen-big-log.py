#!/usr/bin/env python
# SKILL QUEST 심화 시즌 — Lv.8 대형 로그 생성기
# 사용법: python tools/gen-big-log.py            (기본 50만 줄 → data/regression-big.log)
#         python tools/gen-big-log.py --lines 50000   (느린 환경용 축소판 — 오류 개수는 동일)
#
# 오류 개수는 줄 수와 무관하게 항상 같습니다(채점기 기대값 고정):
#   assertion 1842 · timeout 317 · build 96 · env 41 · 스파이크 02:14
import argparse
import random
from datetime import datetime, timedelta

START = datetime(2026, 8, 18, 22, 0, 0)   # 22:00 시작, 8시간(480분) 커버
DURATION_MIN = 480
SPIKE_MINUTE = 254                         # 22:00 + 254분 = 02:14

# (유형, 시그니처, 개수) — 합계: assertion 1842 / timeout 317 / build 96 / env 41
SPREAD_ERRORS = [
    ("assertion", "UVM_ERROR ddr_ctrl.sv(233): assertion 'ref_interval_max' failed", 342),
    ("assertion", "UVM_ERROR ddr_phy.sv(412): assertion 'cal_done_within_2us' failed", 455),
    ("assertion", "UVM_ERROR ddr_pmu.sv(178): assertion 'sr_exit_latency' failed", 301),
    ("assertion", "UVM_ERROR axi_mon.sv(91): assertion 'rvalid_within_16' failed", 230),
    ("assertion", "UVM_ERROR pcie_ltssm.sv(305): assertion 'l0_entry_timeout' failed", 114),
    ("timeout",   "TIMEOUT: watchdog expired after 600s (no activity on m_axi.rvalid)", 201),
    ("timeout",   "TIMEOUT: watchdog expired after 600s (scoreboard queue not drained)", 116),
    ("build",     "BUILD ERROR: vlog-2110 undeclared identifier 'msi_vec_q' (pcie_msi_agent.sv:87)", 63),
    ("build",     "BUILD ERROR: vopt-7 failed to find design unit 'ddr_bist_wrap'", 33),
    ("env",       "ENV ERROR: license checkout failed (VCSRuntime_Net: all seats in use)", 27),
    ("env",       "ENV ERROR: scratch disk quota exceeded on /sim/scratch07 (needed 4.2G)", 14),
]
SPIKE_SIG = "UVM_ERROR ddr_ctrl.sv(233): assertion 'ref_interval_max' failed"

TESTS = ["tb_ddr_refresh", "tb_ddr_init_cal", "tb_axi_outstanding", "tb_pcie_msi",
         "tb_ddr_bist", "tb_ddr_lowpower", "tb_axi_narrow_burst", "tb_pcie_hotplug"]
FILLER = [
    "INFO tb_runner: heartbeat seq={i} queue={q}",
    "INFO scoreboard: compared {n} transactions, mismatches=0",
    "TEST tb_axi_burst_rw ......... PASS  (t=142s)",
    "TEST tb_spi_loopback ......... PASS  (t=41s)",
    "INFO regr_daemon: dispatch batch {b} (16 jobs)",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", type=int, default=500000)
    ap.add_argument("--out", default="data/regression-big.log")
    args = ap.parse_args()
    n = max(args.lines, 20000)

    # 스파이크 크기: 50만 줄 기준 400, 축소판에서는 그 분(minute)의 줄 수에 맞춰 줄임
    lines_per_min = n // DURATION_MIN
    spike_size = min(400, max(40, lines_per_min // 2))
    # 02:14 분에 정확히 들어가는 첫 줄 인덱스 (타임스탬프 역산 — 분 경계에 걸치지 않게)
    spike_start = (SPIKE_MINUTE * 60 * n) // (DURATION_MIN * 60) + 1

    # 스파이크만큼 첫 시그니처 잔여 수량을 조정해 유형별 총계를 고정한다
    spread = []
    for typ, sig, cnt in SPREAD_ERRORS:
        if sig == SPIKE_SIG:
            cnt = cnt + 400 - spike_size
        spread.append((typ, sig, cnt))

    errors = {}
    for k in range(spike_size):
        errors[spike_start + k] = SPIKE_SIG

    seq = []
    for _typ, sig, cnt in spread:
        seq.extend([sig] * cnt)
    random.Random(87231).shuffle(seq)          # 시드 고정 — 매번 같은 파일
    step = n // (len(seq) + 1)
    pos = step
    for sig in seq:
        while pos in errors:                    # 스파이크 자리와 겹치면 한 칸 민다
            pos += 1
        errors[pos] = sig
        pos += step

    with open(args.out, "w", encoding="utf-8") as f:
        for i in range(n):
            ts = START + timedelta(seconds=i * (DURATION_MIN * 60) / n)
            stamp = ts.strftime("[%Y-%m-%d %H:%M:%S]")
            if i in errors:
                test = TESTS[i % len(TESTS)]
                f.write(f"{stamp} TEST {test} FAIL  {errors[i]}\n")
            else:
                tpl = FILLER[i % len(FILLER)]
                f.write(f"{stamp} {tpl.format(i=i, q=i % 37, n=i % 900 + 100, b=i % 240)}\n")

    total_err = len(errors)
    print(f"OK: {args.out}  ({n:,} 줄, 오류 {total_err:,}건, 스파이크 02:14)")
    print("이제 이 파일은 '직접 읽기'에는 너무 큽니다 — 그게 이번 미션의 출발점입니다.")


if __name__ == "__main__":
    main()
