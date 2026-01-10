🛡️ AI Security Analyst Agent

Production-Grade SOAR Microservice

A containerized Security Orchestration, Automation, and Response (SOAR) platform that automatically triages security alerts using AI.
It integrates Splunk (SIEM), Groq / Llama-3 (LLM), and Jira (Ticketing) into a fully automated SOC pipeline.

This is not a demo script — this is a deployment-ready SOC microservice.

🎥 Demo Video
[https://github.com/Naifnizami/AI-Security-Analyst-Agent/blob/main/AI_SOC_Agent_Automated_Triage_Demo.mp4]
If the video does not play inside the GitHub mobile app, tap “View Raw” or download it.

🚀 What This Agent Does

This system acts like a Tier-1 SOC Analyst:

Step	Action
1	Receives security alerts from Splunk via webhook
2	Parses the event and extracts suspicious IPs
3	Determines False Positive vs True Threat
4	Uses Llama-3 (Groq) to investigate real attackers
5	Automatically updates Jira
6	Closes safe alerts or escalates real incidents

No human intervention required.

🧠 Core Capabilities

Production Architecture

Gunicorn WSGI server

4 parallel workers

Runs inside hardened Docker container

Smart Detection

Recognizes trusted IPs (localhost, internal scans)

Flags real external attackers

AI-Powered Investigation

Llama-3 performs threat analysis

Generates incident intelligence reports

SOC Automation

Auto-closes false positives

Creates & escalates real incidents in Jira

🏗️ Architecture
Component	Technology	Purpose
Container	Docker (Debian Slim)	Portable SOC deployment
API Server	Flask + Gunicorn	Receives Splunk alerts
SIEM	Splunk Enterprise	Monitors /var/log/auth.log
AI Engine	Llama-3-70B (Groq)	Threat investigation
Ticketing	Jira Cloud API	Incident management
📦 Quick Start (Production Deployment)
1️⃣ Clone the Repository
git clone https://github.com/Naifnizami/AI-Security-Analyst-Agent.git
cd AI-Security-Analyst-Agent

2️⃣ Configure Secrets
mv .env.example .env


Edit .env:

GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx
JIRA_API_TOKEN=ATxxxxxxxxxxxxxx
JIRA_EMAIL=your_email@example.com

3️⃣ Build the Production Image
sudo docker build -t sec-agent:prod .

4️⃣ Run the SOC Agent
sudo docker run -p 5000:5000 --env-file .env sec-agent:prod


Your AI SOC Analyst is now live.

🧪 How Alerts Are Generated
🔹 Method 1 — Direct Injection (Demo Mode)

Used in the video for speed and isolation testing.

curl -X POST http://127.0.0.1:5000/webhook \
-d '{"result": {"_raw": "Suspicious traffic to 185.196.8.2"}}'


These events bypass Splunk and go directly to the Agent for logic testing.

🔹 Method 2 — Real-World SOC Pipeline

Attacker runs

ssh root@<server-ip>


Linux logs it to

/var/log/auth.log


Splunk detects the failed login

Splunk sends the alert to the Agent

AI investigates and updates Jira

This is true end-to-end SOC automation.

📁 Project Structure
/
├── config/              # Whitelists, rules
├── src/
│   ├── main.py          # Flask webhook + Gunicorn entry
│   └── agent_logic.py   # Llama-3 decision engine
├── Dockerfile          # Production build
├── requirements.txt    # Locked dependencies
└── README.md

⚖️ Disclaimer

This project is for educational and defensive security research only.
You must have explicit authorization to monitor systems or analyze traffic.
