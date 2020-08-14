from statistics import median, mean
from textblob import TextBlob

class Sentiment():
    def calculate_sentiment(self, data: dict) -> dict:
        for video_id in data:
            video = data[video_id]
            polarity = []
            subjectivity = []

            for comment in video["comments"]:
                blob = TextBlob(comment["text"])
                comment["polarity"] = blob.sentiment.polarity
                comment["subjectivity"] = blob.sentiment.subjectivity
                polarity.append(blob.sentiment.polarity)
                subjectivity.append(blob.sentiment.subjectivity)
            
            video["average_polarity"] = mean(polarity)
            video["average_subjectivity"] = mean(subjectivity)
            video["median_polarity"] = median(polarity)
            video["median_subjectivity"] = median(subjectivity)