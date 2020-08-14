import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from .youtube import Youtube
from .sentiment import Sentiment

load_dotenv()
PORT = os.getenv("PORT") or 8000

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
youtube = Youtube()

@app.route('/channel', methods=["GET"])
@cross_origin()
def get_channel():
    channel_name = request.args.get("name")
    channel_id = youtube.get_channel_id(channel_name)

    if not channel_id:
        return jsonify({
            "message": "Failed to find channel."
        }), 400

    return jsonify({
        "channelId": channel_id
    })

@app.route('/sentiment', methods=["GET"])
@cross_origin()
def get_sentiment():
    channel_id = request.args.get('channel')
    
    if not channel_id:
        return jsonify({ "message": "Channel must be provided." }), 400

    sentiment = Sentiment()
    videos = youtube.get_videos(channel_id)

    data = []

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

        data.append({
            "id": video_id,
            "title": video["snippet"]["title"],
            "comments": comments_data
        })
    
    sentiment.calculate_sentiment(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(threaded=True, port=PORT)