import json
import os
import redis
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from .youtube import Youtube
from .sentiment import Sentiment

load_dotenv()
PORT = os.getenv("PORT") or 8000
CACHE_EXPIRY = os.getenv("CACHE_EXPIRY") or 24 * 60 * 60 # By default expires in 24hr

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
youtube = Youtube()
cache = redis.from_url(os.getenv("REDIS_URL"))

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
    invalidate = request.args.get('invalidate') == "true"
    
    if not channel_id:
        return jsonify({ "message": "Channel must be provided." }), 400
    
    # First try to get data from cache
    # TODO: Better strategy for invalidating cache if newer videos have been added.
    # Perhaps cache individual video instead?
    if not invalidate:
        cache_data = cache.get(channel_id)

        if cache_data:
            return jsonify(json.loads(cache_data))

    sentiment = Sentiment()
    videos = youtube.get_videos(channel_id)

    data = {
        "channel": youtube.get_channel_details(channel_id),
        "videos": []
    }

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

        data["videos"].append({
            "id": video_id,
            "title": video["snippet"]["title"],
            "comments": comments_data
        })
    
    sentiment.calculate_sentiment(data["videos"])
    
    # Cache data before returning
    cache.set(channel_id, json.dumps(data), ex=CACHE_EXPIRY)

    return jsonify(data)

if __name__ == "__main__":
    app.run(threaded=True, port=PORT)