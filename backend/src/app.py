import json
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from .youtube import Youtube
from .sentiment import Sentiment

load_dotenv()

app = Flask(__name__)
youtube = Youtube()
PORT = os.getenv("PORT") or 8000

@app.route('/', methods=["GET"])
def get_sentiment():
    channel_name = request.args.get('channel')
    
    if not channel_name:
        return jsonify({ "message": "Channel must be provided." }), 400

    sentiment = Sentiment()
    videos = youtube.get_videos(channel_name)

    data = {}

    for video in videos["items"]:
        print(json.dumps(video["id"], indent=2))
        video_id = video["id"]["videoId"]
        comments = youtube.get_comments(video_id)
        comments_data = []

        for comment in comments["items"]:
            comments_data.append({
                "id": comment["id"],
                "text": comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            })

        data[video_id] = {
            "id": video_id,
            "title": video["snippet"]["title"],
            "comments": comments_data
        }
    
    sentiment.calculate_sentiment(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(threaded=True, port=PORT)