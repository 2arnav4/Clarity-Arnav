from flask import Blueprint, request, jsonify
from services.groq_client import verify_news

news_bp = Blueprint("news", __name__)

@news_bp.route("/verify", methods=["POST"])
def verify():
    try:
        data = request.json
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400
        
        result = verify_news(data["text"])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
