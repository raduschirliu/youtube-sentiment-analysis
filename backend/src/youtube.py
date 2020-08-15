import os
from googleapiclient.discovery import build

class Youtube():
    def __init__(self):
        key = os.getenv("API_KEY")
        dev = os.getenv("DEV") == "true"

        if dev:
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        self.service = build("youtube", "v3", developerKey=key)
    
    def get_channel_id(self, channel_name: str) -> str:
        channel = self.service.channels().list(
            part="snippet",
            forUsername=channel_name
        ).execute()

        if channel == None or "items" not in channel:
            return None

        channel_id = channel["items"][0]["id"]
        return channel_id
    
    def get_channel_details(self, channel_id: str) -> dict:
        channel = self.service.channels().list(
            part="snippet,statistics",
            id=channel_id
        ).execute()
        
        if channel == None or "items" not in channel:
            return None

        return channel["items"][0]
    
    def get_videos(self, channel_id: str) -> dict:
        videos = self.service.search().list(
            part="snippet",
            type="video",
            maxResults=10,
            channelId=channel_id,
            order="date"
        ).execute()

        return videos

    def get_comments(self, video_id: str) -> dict:
        comments = self.service.commentThreads().list(
            part="snippet",
            videoId=video_id,
            order="relevance",
            maxResults=20,
            textFormat="plainText"
        ).execute()

        return comments