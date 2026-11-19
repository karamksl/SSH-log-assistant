# SSH Log Triage Assistant

A Python tool that reads SSH authentication logs and uses Claude API to flag suspicious IP addresses, rate their severity, and recommend mitigations.

IP addresses and usernames are masked before leaving the local machine, and the values are restored locally in the final report.

Python 3.10+
