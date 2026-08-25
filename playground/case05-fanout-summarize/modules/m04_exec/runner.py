import subprocess
def run_report(fmt):
    # 취약점: shell=True + 사용자 입력 (command injection)
    return subprocess.check_output(f"generate_report --format {fmt}", shell=True)
