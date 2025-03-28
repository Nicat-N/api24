from flask import Flask
from flask_cors import CORS 
from .routes import get_news

app = Flask(__name__)

CORS(app, resource={r"/api/news": {
    "orogins": ["https://github.com/Nicat-N"],
    "methods": ["GET"]
}})

@app.route("/api/news", methods={"GET"})
def news_route():
    return get_news()