import requests
import os
import logging

# Setup Logger
logger = logging.getLogger(__name__)

def check_ip_reputation(ip_address: str):
    """
    Checks the reputation of an IP address using AbuseIPDB.
    Useful for validating if a Source IP is a known attacker.
    
    Args:
        ip_address (str): The target IP (e.g., '185.196.8.2')
        
    Returns:
        str: JSON summary of the IP reputation score and usage type.
    """
    api_key = os.environ.get("ABUSEIPDB_API_KEY")
    if not api_key:
        logger.error("AbuseIPDB Key missing.")
        return "Error: AbuseIPDB API Key not found in environment variables."

    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': 90
    }

    try:
        logger.info(f"🔎 Querying AbuseIPDB for: {ip_address}")
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json().get('data', {})
            score = data.get('abuseConfidenceScore', 0)
            country = data.get('countryCode', 'Unknown')
            isp = data.get('isp', 'Unknown')
            usage = data.get('usageType', 'Unknown')
            
            # Formulate a clean summary for the AI
            result = (
                f"AbuseIPDB Threat Intelligence:\n"
                f"- IP: {ip_address}\n"
                f"- Threat Score: {score}/100\n"
                f"- ISP: {isp} ({country})\n"
                f"- Usage Type: {usage}\n"
                f"- Recommendation: {'BLOCK IMMEDIATELY' if score > 50 else 'Investigate'}"
            )
            return result
        else:
            logger.error(f"AbuseIPDB API Error: {response.status_code}")
            return f"Error querying reputation. Code: {response.status_code}"
            
    except Exception as e:
        logger.error(f"Connection Failed: {str(e)}")
        return f"Connection Failed: {str(e)}"
