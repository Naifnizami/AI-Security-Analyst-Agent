from agno.agent import Agent
from agno.models.groq import Groq
# from agno.tools.duckduckgo import DuckDuckGoTools  # <--- Commented out for Demo Stability
import os
import logging

# ==========================================
# 📝 LOGGING SETUP
# ==========================================
logger = logging.getLogger(__name__)

# ==========================================
# 🔑 CONFIGURATION
# ==========================================
os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY") 

# 1. Define the AI Agent (Pure LLM Knowledge Base)
soc_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"), 
    # tools=[DuckDuckGoTools()], # <--- Disabled to prevent rate-limit errors in video
    description="You are an expert SOC Analyst. Your job is to enrich alert data.",
    instructions=[
        "You will be given a Source IP and an Alert Type.",
        "1. Identify if the IP is Public or Private (Local).",
        "2. Analyze the reputation of the IP based on your internal cybersecurity knowledge.",
        "3. Decide: Is this a False Positive (Safe) or True Positive (Threat)?",
        "4. Output your finding as a concise paragraph.",
    ],
    markdown=True
)

# 2. Function to be called by your main script
def investigate_ip(ip, alert_name):
    query = f"Investigate this IP: {ip}. The alert is: {alert_name}"
    try:
        # Use professional logger
        logger.info(f"🤖 AI is thinking about {ip}...")
        
        response = soc_agent.run(query)
        return response.content
        
    except Exception as e:
        logger.error(f"AI Error during investigation: {str(e)}")
        return f"AI Error: {str(e)}"

# 3. Quick Test (Only runs if you run this file directly)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("--- TEST MODE ---")
    logger.info(investigate_ip("8.8.8.8", "DNS Modification"))
