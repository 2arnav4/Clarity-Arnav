# File: Backend/routes/news.py

from flask import Blueprint, request, jsonify
# --- IMPORT the renamed function from the renamed file ---
# from services.groq_client import verify_news
from services.openrouter_client import get_verification_from_openrouter
# --- END IMPORT CHANGE ---

news_bp = Blueprint("news", __name__)

@news_bp.route("/verify", methods=["POST"])
def verify():
    # Keep existing print statements or add more if needed
    print("--- Received request for /verify ---")
    try:
        data = request.json
        print(f"Request data: {data}")
        if not data or "text" not in data:
            print("Error: Missing 'text' field in request data")
            return jsonify({"error": "Missing 'text' field"}), 400

        text_to_verify = data["text"]
        print(f"Text to verify: '{text_to_verify}'")

        # --- CALL the new function ---
        print("Calling get_verification_from_openrouter service...")
        result = get_verification_from_openrouter(text_to_verify)
        # --- END FUNCTION CALL CHANGE ---

        print(f"Service returned: {result}")
        # Return the result obtained from OpenRouter
        # The frontend might need adjustment based on this structure
        return jsonify(result)

    except ConnectionError as conn_err: # Catch specific connection error from the service
        print(f"!!! CONNECTION ERROR in /verify route: {conn_err}")
        print(f"Exception type: {type(conn_err)}")
        # Return 503 Service Unavailable if connection fails
        return jsonify({"error": str(conn_err)}), 503
    except ValueError as val_err: # Catch ValueErrors (e.g., missing API key, missing text)
        print(f"!!! VALUE ERROR in /verify route: {val_err}")
        print(f"Exception type: {type(val_err)}")
        # Return 400 Bad Request for validation errors
        return jsonify({"error": str(val_err)}), 400
    except Exception as e: # Catch other errors (like HTTP errors from OpenRouter)
        print(f"!!! EXCEPTION OCCURRED in /verify route: {e}")
        print(f"Exception type: {type(e)}")
        # Return 500 Internal Server Error for unexpected issues
        return jsonify({"error": str(e)}), 500