"""
Multi-Threaded Network Reconnaissance & Port Scanner
Author: SpectraOne Solutions (https://spectraonesolutions.com)
Description: Lightweight socket-based port scanner for defensive auditing and penetration testing prep.
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Common ports and their standard services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
}

def scan_port(target_ip: str, port: int, timeout: float = 1.0):
    """Scans a single port on the target IP and checks for open status."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                service = COMMON_PORTS.get(port, "Unknown Service")
                print(f" [+] Port {port:<5} | OPEN | Service: {service}")
                return port
    except socket.error:
        pass
    return None

def run_port_scan(target_host: str, max_threads: int = 50):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[!] Hostname could not be resolved: {target_host}")
        sys.exit(1)

    print("=" * 65)
    print(f"🎯 NETWORK AUDIT SCANNER — SPECTRAONE SOLUTIONS")
    print(f" Target Host : {target_host} ({target_ip})")
    print(f" Scan Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 65)

    open_ports = []
    ports_to_scan = list(COMMON_PORTS.keys())

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in ports_to_scan]
        for future in futures:
            res = future.result()
            if res:
                open_ports.append(res)

    print("-" * 65)
    print(f"Scan complete. Total Open Ports Found: {len(open_ports)}")
    print("=" * 65)

if __name__ == "__main__":
    # Example scan against local loopback or change to authorized target IP
    target = "127.0.0.1"
    run_port_scan(target)
