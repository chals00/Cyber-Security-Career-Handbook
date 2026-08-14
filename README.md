# 🛡️ Practical Cyber Security & SOC Analyst Career Handbook (2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Maintained by SpectraOne Solutions](https://img.shields.io/badge/Maintained%20by-SpectraOne%20Solutions-orange)](https://spectraonesolutions.com)

A comprehensive, industry-aligned roadmap and practical resource repository for mastering **Cyber Security**, **SOC Analysis (L1/L2)**, **Threat Hunting**, **Network Defense**, and **Incident Response**. Curated and maintained by [SpectraOne Solutions](https://spectraonesolutions.com).

---

## 🗺️ 2026 Cyber Security & Defense Roadmap

### Phase 1: Networking & Systems Fundamentals
* **Networking Protocols:** TCP/IP stack, OSI Model, DNS, DHCP, HTTP/S, SSH, ARP, and ICMP.
* **Network Traffic Analysis:** Packet capture inspection with **Wireshark** and `tcpdump`.
* **OS Administration & Command Line:** Linux fundamentals (permissions, systemd, bash scripting) and Windows Active Directory basics.

### Phase 2: Security Operations & SIEM
* **Security Information & Event Management (SIEM):** Splunk, Elastic SIEM, and Microsoft Sentinel.
* **Log Analysis:** Parsing syslog, Windows Event Logs (4624, 4625, 4720), and firewall access logs.
* **Frameworks & Threat Intelligence:** MITRE ATT&CK Framework, Cyber Kill Chain, NIST Cybersecurity Framework, and CVE analysis.

### Phase 3: Defensive Engineering & Incident Response
* **Incident Response Lifecycle:** Preparation, Identification, Containment, Eradication, Recovery, and Lessons Learned (NIST SP 800-61).
* **Endpoint Detection & Response (EDR):** Threat triaging, malware process analysis, and persistence mechanism detection.
* **Identity & Access Management (IAM):** Role-Based Access Control (RBAC), Multi-Factor Authentication (MFA), and Zero-Trust architecture.

### Phase 4: Ethical Hacking & Vulnerability Assessment
* **Reconnaissance & Scanning:** `nmap`, `masscan`, and vulnerability scanners like OpenVAS / Nessus.
* **Web Application Security:** OWASP Top 10 (SQL Injection, XSS, Broken Access Control, CSRF).
* **Remediation & Hardening:** Patch management strategies and security baseline configurations (CIS Benchmarks).

---

## 📁 Included Security Assets & Tooling
* [`soc_auth_log_analyzer.py`](./soc_auth_log_analyzer.py) — Automated Python security script to parse server authentication logs and detect brute-force attack attempts.
* [`incident_response_checklist.md`](./incident_response_checklist.md) — Step-by-step triage checklist for handling containment and remediation during security alerts.

---

## 🎯 Top Cyber Security Technical Interview Questions

### 1. What happens during a TCP Three-Way Handshake?
* **SYN:** Client sends a Synchronize packet with an initial sequence number.
* **SYN-ACK:** Server responds with a Synchronize-Acknowledgment packet.
* **ACK:** Client acknowledges the server's response, establishing the connection.
* *Security context:* SYN Flood attacks exploit this by never sending the final ACK, exhausting server connection queues.

### 2. How do you distinguish between a False Positive and a True Positive alert in a SIEM?
* **True Positive:** The alert fired on legitimate malicious or unauthorized activity requiring escalation.
* **False Positive:** The alert fired due to benign activity (e.g., a scheduled administrative script, misconfigured scanner, or standard user behavior).

### 3. What is the difference between Symmetric and Asymmetric Encryption?
* **Symmetric:** Uses the same shared secret key for encryption and decryption (e.g., AES-256). Fast and suited for bulk data.
* **Asymmetric:** Uses a mathematically linked key pair—a public key to encrypt and a private key to decrypt (e.g., RSA, ECC). Essential for key exchange and digital signatures.

---

## 🚀 Accelerate Your Cyber Security Career with Live Training

Looking for instructor-led, hands-on training with virtual labs and live incident simulations?

* 🌐 **Website:** [SpectraOne Solutions](https://spectraonesolutions.com)
* 🎓 **Core Career Tracks:**
  * [Cyber Security & Defense Training](https://spectraonesolutions.com)
  * [Quality Assurance & SDET Training](https://spectraonesolutions.com)
  * [Data Science & Business Analytics Training](https://spectraonesolutions.com)
  * [Java Backend Developer Training](https://spectraonesolutions.com)
  * [AI & Automation Engineering Training](https://spectraonesolutions.com)

---

## 🤝 Contributing
Contributions, additional analysis scripts, and interview prep questions are welcome! Feel free to open a Pull Request.
