# File: Backend/services/groq_client.py (Consider renaming to llm_client.py)

import requests
import os
# from dotenv import load_dotenv # No longer strictly needed for Ollama key

# load_dotenv() # No longer strictly needed for Ollama key

# GROQ_API_KEY = os.getenv("GROQ_API_KEY") # No longer needed for Ollama

# --- OLLAMA Configuration ---
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions" # Default Ollama OpenAI endpoint
# Make sure you have pulled this model in Ollama (e.g., ollama pull llama3)
OLLAMA_MODEL = "llama3" # <-- CHANGE TO YOUR DESIRED OLLAMA MODEL
# --- End OLLAMA Configuration ---

# Consider renaming this function, e.g., get_llm_verification
def verify_news(text):
    print("--- Entered verify_news function (using Ollama) ---")

    if not text:
        print("Error: No text provided to verify_news")
        raise ValueError("No text provided for verification")

    # Construct the payload expected by the Ollama chat completions endpoint
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            # You can add a system prompt here if desired
            # {
            #     "role": "system",
            #     "content": "You are a helpful fact-checking assistant..."
            # },
            {
                "role": "user",
                "content": f"Please fact-check this news headline/text: \"{text}\"" # Embed the user's text
            }
        ],
        "stream": False, # Explicitly disable streaming if you want the full response at once
        # Add other Ollama-specific parameters if needed (check Ollama API docs)
    }
    print(f"Sending payload to Ollama API: {payload}")

    try:
        response = requests.post(
            OLLAMA_API_URL,
            json=payload,
            # No Authorization header needed for default local Ollama
        )

        print(f"Ollama API response status code: {response.status_code}")
        print(f"Ollama API response text (raw): {response.text}")

        # Raise an exception for bad status codes (like 4xx client errors or 5xx server errors)
        response.raise_for_status()

        result_json = response.json()
        print(f"Ollama API response JSON: {result_json}")

        # IMPORTANT: Extract the actual message content from the response
        # This structure might vary slightly depending on Ollama version/settings
        try:
            # Attempt to get the content from the first choice's message
            content = result_json.get('choices', [{}])[0].get('message', {}).get('content', '')
            print(f"Extracted content: {content}")
            # You might want to return just the content or a structured dict
            # For now, returning the whole JSON, but adjust as needed for your frontend
            return result_json
            # Example of returning just the content string:
            # return {"verification_result": content}
        except (IndexError, AttributeError, KeyError) as e:
             print(f"Error parsing Ollama response structure: {e}")
             raise Exception("Failed to parse expected content from Ollama response")


    except requests.exceptions.RequestException as req_err: # Handle connection errors etc.
        print(f"!!! REQUESTS EXCEPTION occurred during Ollama API call: {req_err}")
        print(f"Is the Ollama server running at {OLLAMA_API_URL}?")
        print(f"Exception type: {type(req_err)}")
        # Raise a clearer exception to be caught by the Flask route
        raise ConnectionError(f"Could not connect to Ollama server at {OLLAMA_API_URL}: {req_err}")
    except Exception as e: # Catch other unexpected errors
        print(f"!!! UNEXPECTED EXCEPTION occurred during Ollama API call: {e}")
        print(f"Exception type: {type(e)}")
        raise # Re-raise    