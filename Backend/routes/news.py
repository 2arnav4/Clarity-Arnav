# File: Backend/routes/news.py

from flask import Blueprint, request, jsonify, current_app
from services.openrouter_client import get_verification_from_openrouter
# --- Import BOTH functions from news_fetcher ---
from services.news_fetcher import get_hardcoded_news, find_hardcoded_news_by_id
# --- END IMPORT ---

news_bp = Blueprint("news", __name__)

# --- Trending News Route (uses fetch_aggregated_news) ---
@news_bp.route("/trending", methods=["GET"])
def get_trending_news():
    """Endpoint to get aggregated trending news (from hardcoded source)."""
    try:
        keywords = request.args.get('keywords', None)
        # Call the fetcher which now uses hardcoded data
        result = get_hardcoded_news() # Pass keywords if implemented

        if "error" in result:
             # If error occurred loading data
             return jsonify({"error": result["error"]}), 500

        return jsonify(result) # Should contain {"articles": [...], "fetch_errors": None}

    except Exception as e:
        current_app.logger.error(f"Error in /trending route: {e}")
        return jsonify({"error": f"An internal server error occurred: {str(e)}"}), 500

# --- NEW ROUTE for fetching single news item by ID ---
@news_bp.route("/<string:item_id>", methods=["GET"])
def get_single_news_item(item_id):
    """Endpoint to get a single news item by its ID."""
    try:
        article = find_hardcoded_news_by_id(item_id)
        if article:
            return jsonify(article)
        else:
            return jsonify({"error": "Article not found"}), 404
    except Exception as e:
        current_app.logger.error(f"Error in /news/<id> route for ID {item_id}: {e}")
        return jsonify({"error": f"An internal server error occurred: {str(e)}"}), 500
# --- END NEW ROUTE ---


# --- Verify Route (Keep as is) ---
@news_bp.route("/verify", methods=["POST"])
def verify():
    # ... (Keep the existing verify implementation using OpenRouter) ...
    print("--- Received request for /verify ---")
    try:
        data = request.json
        print(f"Request data: {data}")
        if not data or "text" not in data:
            print("Error: Missing 'text' field in request data")
            return jsonify({"error": "Missing 'text' field"}), 400

        text_to_verify = data["text"]
        print(f"Text to verify: '{text_to_verify}'")
        print("Calling get_verification_from_openrouter service...")
        result = get_verification_from_openrouter(text_to_verify)
        print(f"Service returned: {result}")
        return jsonify(result)

    except ConnectionError as conn_err:
        print(f"!!! CONNECTION ERROR in /verify route: {conn_err}")
        print(f"Exception type: {type(conn_err)}")
        return jsonify({"error": str(conn_err)}), 503
    except ValueError as val_err:
        print(f"!!! VALUE ERROR in /verify route: {val_err}")
        print(f"Exception type: {type(val_err)}")
        return jsonify({"error": str(val_err)}), 400
    except Exception as e:
        print(f"!!! EXCEPTION OCCURRED in /verify route: {e}")
        print(f"Exception type: {type(e)}")
        current_app.logger.error(f"Exception in /verify route: {e}", exc_info=True)
        return jsonify({"error": f"An internal server error occurred: {str(e)}"}), 500