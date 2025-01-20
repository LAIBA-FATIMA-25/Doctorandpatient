import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "kkkk")  # Replace with your actual API key

def call_llm(prompt: str) -> str:
    """
    Calls the Gemini API to process the prompt and fetch the response.
    """
    url = "https://api.gemini.com/v1/llm"  # Hypothetical endpoint
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"prompt": prompt}

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("response", "No response received.")
    else:
        return f"Error: {response.status_code}, {response.text}"
