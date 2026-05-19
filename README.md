🛡️ VulnSpecter – Cyber Vulnerability Scanner

VulnSpecter is a lightweight cybersecurity tool that scans websites for common vulnerabilities and visualizes the results through a cyber-style dashboard with an attack risk meter.

The project demonstrates concepts used in professional security tools like OWASP ZAP and Nmap, but in a simplified and educational form.

It helps identify:

Missing security headers
Sensitive files exposed
Admin panel endpoints
Open ports
Web technologies used
Overall vulnerability risk score
🚀 Live Application

Try the deployed scanner here:

VulnSpecter Dashboard

Open VulnSpecter App

🧠 Project Purpose

The goal of VulnSpecter is to help learners understand:

Basic penetration testing techniques
Web security misconfigurations
How vulnerability scanners work internally
How cybersecurity dashboards visualize risks

It acts as a mini penetration testing assistant.

⚡ Key Features
🔍 Web Vulnerability Detection

Scans target websites for:

Exposed sensitive files
Admin login panels
Missing HTTP security headers
🖥️ Cyber Security Dashboard

Interactive interface built with Streamlit.

Features include:

Scan results visualization
Security status indicators
Attack logs
⚠️ Attack Risk Meter

A dynamic risk scoring system that calculates the severity of discovered vulnerabilities.

Example output:

Risk Score: 65%
Threat Level: HIGH
🧠 Technology Detection

Identifies server technologies used by the target.

Examples:

Server: Apache
Framework: PHP
Platform: Linux
🌐 Port Scanner

Performs lightweight network checks similar to tools like Nmap.

Example ports checked:

80   → HTTP
443  → HTTPS
21   → FTP
22   → SSH
📄 Vulnerability Report

Automatically generates a structured vulnerability report showing:

Findings
Risk level
Security recommendations
🛠️ Technology Stack
Technology	Purpose
Python	Core programming language
Streamlit	Dashboard interface
Requests	HTTP scanning
Socket	Port scanning
Pandas	Data handling
ReportLab	Report generation
📂 Project Structure
vulnspecter
│
├── app.py                # Streamlit dashboard
├── scanner.py            # Main scanning engine
├── checks.py             # Vulnerability checks
├── risk.py               # Risk score calculation
├── port_scan.py          # Port scanner
├── tech_detect.py        # Technology detection
├── report.py             # Report generator
├── utils.py              # Helper functions
│
├── requirements.txt
├── README.md
│
└── assets
    └── cyber.css         # Cyber theme styling
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/vulnspecter.git
cd vulnspecter

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run app.py

The app will start locally:

http://localhost:8501
🧪 Example Test Targets

Use intentionally vulnerable websites for safe testing.

Example:

http://testphp.vulnweb.com
http://demo.testfire.net

These environments are commonly used with security tools like Burp Suite.

📊 Example Scan Output
Sensitive Files: FOUND
Admin Panels: FOUND
Security Headers: MISSING

Open Ports
80  → HTTP
443 → HTTPS

Technology
Server: Apache

Risk Score
72% → HIGH
🔐 Ethical Use Disclaimer

This tool is intended only for educational purposes.

Only scan:

Your own websites
Local test environments
Intentionally vulnerable labs

Never scan websites without permission.

🌟 Future Improvements

Possible enhancements:

CVSS vulnerability scoring
Real-time attack radar visualization
Subdomain discovery
API security scanning
Automated PDF reports
