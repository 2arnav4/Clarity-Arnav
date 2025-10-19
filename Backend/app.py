from flask import Flask
from routes.news import news_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

app.register_blueprint(news_bp, url_prefix="/api/news")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
