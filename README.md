# 🛡️ AI-Powered SOAR Engine: Splunk ➡️ Jira ➡️ Agno (Llama 3)
> **Agentic Security Incident Response & Threat Enrichment Pipeline**

## 🎥 Project Demo (V4 Agentic AI)
**[CLICK HERE TO WATCH THE LIVE DEMO](https://github.com/Naifnizami/SOAR-EDR-Automation-Lab/blob/main/SOC_Agno_Project.mp4)**

## In this video:
1.  **False Positive:** Attack from localhost is detected and **Auto-Closed** instantly.
2.  **True Positive:** Attack from an external network triggers the **AI Agent**, which investigates the IP context and writes a threat report in Jira.

> **📱 Viewing Tip:** *For the best clarity of the terminal text, please view this video on **Mobile** or **download the raw file**, as GitHub's web player compresses the 720p text on desktops.*

---

## 📝 Project Overview
This project evolves the traditional SOC playbook from "Static Automation" to "Agentic Intelligence."

In **Version 4**, I ripped out the hard-coded logic and integrated an autonomous AI Agent (**Agno/Llama-3**) to act as a Tier 1 Analyst. The Agent actively investigates source IPs, determines context (Private vs Public network), scans for threat reputation, and writes a human-readable investigation report directly into the **Jira** ticket.

### 🧠 V4.0 Agentic Capabilities
*   **🤖 AI Analyst Integration:** Utilizes **Agno (formerly Phidata)** running the **Llama-3-70b** model via **Groq LPU** for sub-second inference.
*   **🔍 Autonomous Investigation:** The Agent distinguishes between internal authorized scans (Private IPs) and external threats. It performs web searches (DuckDuckGo) to validate reputation.
*   **📝 Natural Language Reporting:** Instead of dumping raw JSON logs, the system creates Jira tickets with a written "Analyst Report" summarizing the findings.

### ⚡ Core Automation Features
*   **Self-Healing Triage:** False Positives (Whitelist/Internal IPs) are auto-ticketed and immediately transitioned to **DONE** (Closed) to prevent analyst fatigue.
*   **Loop Prevention:** Splunk alerting optimized with precise cron scheduling (`-1m@m`) to eliminate duplicate alerts for the same event.

## 🛠️ Tech Stack
*   **SIEM:** Splunk Enterprise 10.x
*   **AI Framework:** Agno (Phidata)
*   **LLM Engine:** Groq API (Llama-3.3-70b-versatile)
*   **Development:** Python 3 (Flask, Requests, RegEx)
*   **Infrastructure:** Kali Linux, Jira Cloud API

## 🔧 Installation & Usage
1.  **Clone the Repo:**
    ```bash
    git clone https://github.com/Naifnizami/SOAR-EDR-Automation-Lab.git
    cd SOAR-EDR-Automation-Lab
    ```
2.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Credentials:**
    *   Set your `JIRA_API_TOKEN` and `GROQ_API_KEY` as environment variables (Recommended).
    *   Update `WHITELIST_IPS` in `soar_engine.py` with your trusted assets.
4.  **Run the Engine:**
    ```bash
    python3 soar_engine.py
    ```
5.  **Configure Splunk:** Point Webhook action to `http://<your-ip>:5000/webhook`.

---

## 🏗️ Architecture Flow (V4)
```mermaid
graph TD
    A[Attacker] -->|SSH Brute Force| B(Kali Linux Logs)
    B -->|Splunk Monitor| C{Splunk Enterprise}
    C -->|Webhook Alert| D[Python SOAR Engine]
    
    subgraph AIBrain [The AI Brain - Agno + Groq]
        D -->|Send IP & Context| E{"AI Agent (Llama 3)"}
        E -->|Reasoning Process| F[Check Context / OSINT]
        F -->|Return Analysis| D
    end
    
    D -- "Analysis: Safe" --> G[Auto-Close Ticket]
    D -- "Analysis: Threat" --> H[Escalate to High Priority]
    
    G -->|API| I[Jira Board: DONE]
    H -->|API + AI Report| J[Jira Board: TO DO]
