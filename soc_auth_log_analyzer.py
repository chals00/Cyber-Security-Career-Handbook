"""
SOC Analyst Log Analyzer & Brute Force Detection Tool
Author: SpectraOne Solutions (https://spectraonesolutions.com)
Description: Lightweight security automation script to identify suspicious failed login spikes.
"""

import re
from collections import defaultdict

# Sample authentication log data (simulating Linux /var/log/auth.log)
SAMPLE_LOGS = """
Aug 14 14:02:11 server sshd[1234]: Failed password for invalid user admin from 192.168.1.105 port 54321 ssh2
Aug 14 14:02:13 server sshd[1235]: Failed password for invalid user root from 192.168.1.105 port 54322 ssh2
Aug 14 14:02:16 server sshd[1236]: Failed password for invalid user root from 192.168.1.105 port 54323 ssh2
Aug 14 14:02:20 server sshd[1237]: Failed password for invalid user test from 192.168.1.105 port 54324 ssh2
Aug 14 14:02:22 server sshd[1238]: Failed password for invalid user oracle from 192.168.1.105 port 54325 ssh2
Aug 14 14:03:01 server sshd[1239]: Accepted password for deployer from 10.0.0.12 port 43210 ssh2
Aug 14 14:04:10 server sshd[1240]: Failed password for valid user john from 172.16.0.45 port 51234 ssh2
"""

FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
)

def analyze_auth_logs(log_data: str, alert_threshold: int = 3):
    failed_attempts_by_ip = defaultdict(int)
    targeted_usernames = defaultdict(set)

    for line in log_data.strip().split("\n"):
        match = FAILED_LOGIN_PATTERN.search(line)
        if match:
            user, ip = match.groups()
            failed_attempts_by_ip[ip] += 1
            targeted_usernames[ip].add(user)

    print("=" * 65)
    print("🚨 SOC INCIDENT REPORT: AUTHENTICATION AUDIT")
    print("=" * 65)

    alerts_triggered = 0
    for ip, count in failed_attempts_by_ip.items():
        if count >= alert_threshold:
            alerts_triggered += 1
            users_list = ", ".join(targeted_usernames[ip])
            print(f"[ALERT] Potential Brute Force Detected!")
            print(f" └── Source IP       : {ip}")
            print(f" └── Failed Attempts : {count}")
            print(f" └── Targeted Users  : {users_list}")
            print(f" └── Recommendation  : Temporarily block IP via iptables / firewall rule.\n")

    if alerts_triggered == 0:
        print("✅ No suspicious brute-force activity exceeding the threshold.")
    print("=" * 65)

if __name__ == "__main__":
    analyze_auth_logs(SAMPLE_LOGS, alert_threshold=3)
