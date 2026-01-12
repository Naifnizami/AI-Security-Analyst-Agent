from agno.agent import Agent
from agno.models.groq import Groq
from .tools import check_ip_reputation  # <--- IMPORT THE NEW TOOL
import os
import logging

# Logger Setup
logger = logging.getLogger(__name__)

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY") 

# 1. Define the AI Agent
soc_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"), 
    
    # Enable the new tool
    tools=[check_ip_reputation],
    
    description="You are an expert SOC Analyst. Your job is to enrich alert data with real Threat Intelligence.",
    instructions=[
        "You will be given a Source IP and an Alert Type.",
        "1. Identify if the IP is Public or Private (Local).",
        "2. If the IP is Public, ALWAYS use the `check_ip_reputation` tool to scan it.",
        "3. Incorporate the AbuseIPDB Threat Score directly into your final report.",
        "4. Output your finding as a professional incident summary.",
    ],
    markdown=True
)

# 2. Function called by main.py
def investigate_ip(ip, alert_name):
    query = f"Investigate this IP: {ip}. The alert is: {alert_name}"
    try:
        logger.info(f"🤖 AI is investigating {ip}...")
        response = soc_agent.run(query)
        return response.content
    except Exception as e:
        logger.error(f"AI Error: {str(e)}")
        return f"AI Error: {str(e)}"

# 3. Quick Test
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("--- TEST MODE ---")
    logger.info(investigate_ip("185.196.8.2", "SSH Brute Force"))
