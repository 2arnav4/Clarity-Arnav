from flask import Blueprint, request, jsonify
from Backend.services.llm_client import verify_news

news_bp = Blueprint("news", __name__)

@news_bp.route("/verify", methods=["POST"])
def verify():
    print("--- Received request for /verify ---") # ADD THIS
    try:
        data = request.json
        print(f"Request data: {data}") # ADD THIS
        if not data or "text" not in data:
            print("Error: Missing 'text' field in request data") # ADD THIS
            return jsonify({"error": "Missing 'text' field"}), 400

        text_to_verify = data["text"]
        print(f"Text to verify: '{text_to_verify}'") # ADD THIS
        print("Calling verify_news service...") # ADD THIS
        result = verify_news(text_to_verify)
        print(f"Service returned: {result}") # ADD THIS
        return jsonify(result)
    except Exception as e:
        print(f"!!! EXCEPTION OCCURRED in /verify route: {e}") # MODIFY THIS
        # Also print the type of exception
        print(f"Exception type: {type(e)}") # ADD THIS
        return jsonify({"error": str(e)}), 500