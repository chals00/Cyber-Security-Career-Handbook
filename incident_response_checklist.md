# 🚨 SOC Incident Response & Triage Checklist (NIST SP 800-61)

[![Maintained by SpectraOne Solutions](https://img.shields.io/badge/Maintained%20by-SpectraOne%20Solutions-orange)](https://spectraonesolutions.com)

A standardized operational triage checklist for Security Operations Center (SOC) Tier-1/Tier-2 analysts during active security incidents.

---

## Phase 1: Detection & Initial Triage
- [ ] **Verify Alert Legitimacy:** Confirm whether the SIEM/EDR alert is a True Positive or False Positive.
- [ ] **Identify Scope:** Document affected hostnames, IP addresses, user accounts, and timestamps.
- [ ] **Determine Severity Level:**
  - **Sev 1 (Critical):** Active ransomware, domain controller compromise, customer PII data exfiltration.
  - **Sev 2 (High):** Malware execution on production servers, compromised administrative credentials.
  - **Sev 3 (Medium/Low):** Isolated phishing click on unprivileged workstation (blocked by EDR).
- [ ] **Open Incident Ticket:** Log IOCs (Indicators of Compromise) including SHA-256 hashes, malicious domains, and source IPs.

---

## Phase 2: Containment & Isolation
- [ ] **Network Isolation:** Disconnect the compromised endpoint from the network via EDR console (do NOT power off the machine to preserve volatile RAM memory).
- [ ] **Account Revocation:** Force sign-out across all active sessions and reset passwords for compromised user accounts.
- [ ] **Perimeter Defense:** Add malicious external IP addresses/domains to the perimeter firewall and web proxy blocklists.
- [ ] **Segment Affected VLAN:** If lateral movement is suspected, isolate the entire subnet.

---

## Phase 3: Eradication & Forensic Collection
- [ ] **Volatile Memory Capture:** Extract memory dumps (`FTK Imager` / `Volatility`) for forensic analysis.
- [ ] **Malware Removal:** Terminate malicious parent/child processes and delete malicious binaries from disk.
- [ ] **Persistence Checks:**
  - [ ] Inspect Scheduled Tasks & Cron jobs.
  - [ ] Audit Windows Registry Run keys (`HKLM\Software\Microsoft\Windows\CurrentVersion\Run`).
  - [ ] Audit new local admin accounts or modified SSH authorized keys.

---

## Phase 4: Recovery & System Restoration
- [ ] **Rebuild / Re-image:** Re-image affected endpoints from trusted, hardened gold-image backups.
- [ ] **Patch Vulnerability:** Apply security patches to the initial exploit vector (e.g., outdated software or missing MFA).
- [ ] **Re-introduce to Production:** Reconnect endpoints and monitor logs closely for 48–72 hours for recurrence.

---

## Phase 5: Post-Incident Review (Lessons Learned)
- [ ] Conduct a post-mortem review meeting within 5 business days.
- [ ] Document root-cause analysis (RCA) report.
- [ ] Update SIEM detection rules and YARA signatures to prevent recurrence.

---

*Curated for security professionals by [SpectraOne Solutions](https://spectraonesolutions.com).*
