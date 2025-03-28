from flask import jsonify, request
from .config import API_KEY
from .models import news_list

def get_news():

    data = [{""tit": news.tit, "des":news.des, "img": news.img"} for news in news_list]

    api_key = request.args.get("api_key")

    if api_key is None and len(request.args) > 0:
        return jsonify({"error": "Invalid quary parameters"})

    if api_key and api_key != API_KEY:
        return jsonify({"error": "Invalid api key"})

    return jsonify({"news": news_data})
