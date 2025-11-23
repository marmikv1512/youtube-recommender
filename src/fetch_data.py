
from googleapiclient.discovery import build
import pandas as pd

API_KEY = "AIzaSyC33wzqYtgZQPmdVr_iCmhbfsuYOxzDTr4"   # paste your key here

def fetch_youtube_videos(query="technology", max_results=50):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )

    response = request.execute()

    videos = []

    for item in response['items']:
        videos.append({
            "videoId": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "thumbnail": item["snippet"]["thumbnails"]["high"]["url"]
        })

    df = pd.DataFrame(videos)
    df.to_csv("videos.csv", index=False)

    print("Saved videos.csv successfully!")

# Run the function
fetch_youtube_videos()
