import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1"  

def verify_news(text):
    if not text:
        raise ValueError("No text provided for verification")
    
    response = requests.post(
        GROQ_API_URL,
        json={"text": text},
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"}
    )
    
    if response.status_code != 200:
        raise Exception(f"GROQ API error: {response.status_code} - {response.text}")
    
    return response.json()
