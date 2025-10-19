# File: Backend/services/openrouter_client.py

import requests
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

# --- OpenRouter Configuration ---
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# IMPORTANT: Choose a model available on OpenRouter
# Example: "mistralai/mistral-7b-instruct", "google/gemma-7b-it", "meta-llama/llama-3-8b-instruct"
# Check OpenRouter documentation/models page for available models
OPENROUTER_MODEL = "mistralai/mistral-7b-instruct" # <-- CHANGE TO YOUR DESIRED MODEL

# Recommended headers for OpenRouter
# Replace 'YOUR_SITE_URL' and 'YOUR_APP_NAME' appropriately
OPENROUTER_HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "http://localhost:8080", # Or your actual frontend URL
    "X-Title": "FactCheck", # Or your app's name
    "Content-Type": "application/json"
}
# --- End OpenRouter Configuration ---


# Renamed function
def get_verification_from_openrouter(text):
    print("--- Entered get_verification_from_openrouter function ---")
    if not OPENROUTER_API_KEY:
        print("!!! ERROR: OPENROUTER_API_KEY is missing from environment variables!")
        raise ValueError("OpenRouter API key not configured")
    print(f"API Key loaded: {'Exists'}") # Basic confirmation

    if not text:
        print("Error: No text provided for verification")
        raise ValueError("No text provided for verification")

    # Construct the payload expected by the chat completions endpoint
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            # You can add a system prompt here if desired
            {
                 "role": "system",
                 "content": "You are a fact-checking assistant. Analyze the provided text and classify it as 'verified', 'misinformation', or 'unverified'. Provide a brief reasoning."
            },
            {
                "role": "user",
                "content": f"Please fact-check this news headline/text: \"{text}\""
            }
        ],
        # Add other parameters like temperature, max_tokens if needed (check OpenRouter docs)
        # "temperature": 0.7,
        # "max_tokens": 200,
    }
    print(f"Sending payload to OpenRouter API: {payload}")

    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers=OPENROUTER_HEADERS,
            json=payload
        )

        print(f"OpenRouter API response status code: {response.status_code}")
        print(f"OpenRouter API response text (raw): {response.text}")

        # Raise an exception for bad status codes (4xx client errors or 5xx server errors)
        response.raise_for_status()

        result_json = response.json()
        print(f"OpenRouter API response JSON: {result_json}")

        # --- IMPORTANT ---
        # Extract the actual message content from the response
        # This structure should be standard OpenAI format
        try:
            content = result_json.get('choices', [{}])[0].get('message', {}).get('content', '')
            print(f"Extracted content: {content}")
            # Consider parsing 'content' to get a structured status and reasoning
            # For now, returning the whole JSON or just the content string might be okay
            # depending on how the frontend will use it.
            # Example: Return a dictionary with the raw content
            return {"verification_result": content, "raw_response": result_json}
        except (IndexError, AttributeError, KeyError) as e:
             print(f"Error parsing OpenRouter response structure: {e}")
             raise Exception("Failed to parse expected content from OpenRouter response")


    except requests.exceptions.HTTPError as http_err: # Catch HTTP errors specifically
        print(f"!!! HTTP ERROR occurred during OpenRouter API call: {http_err}")
        print(f"Response Body: {response.text}") # Print response body on HTTP error
        print(f"Exception type: {type(http_err)}")
        raise Exception(f"OpenRouter API Error: {http_err.response.status_code} - {response.text}")
    except requests.exceptions.RequestException as req_err: # Handle connection errors etc.
        print(f"!!! REQUESTS EXCEPTION occurred during OpenRouter API call: {req_err}")
        print(f"Exception type: {type(req_err)}")
        raise ConnectionError(f"Could not connect to OpenRouter API at {OPENROUTER_API_URL}: {req_err}")
    except Exception as e: # Catch any other unexpected errors
        print(f"!!! UNEXPECTED EXCEPTION occurred during OpenRouter API call: {e}")
        print(f"Exception type: {type(e)}")
        raise