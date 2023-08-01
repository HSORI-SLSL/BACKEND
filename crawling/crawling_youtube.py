from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyACXUW6TG--uaoGqzuTR7o7CoYwl861VwY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

import json

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=options,
        part="id,snippet",
        maxResults=5  # Set the number of search results you want to retrieve (in this case, 5)
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_id = search_result["id"]["videoId"]
            video_title = search_result["snippet"]["title"]
            channel_id = search_result["snippet"]["channelId"]
            thumbnail_url = search_result["snippet"]["thumbnails"]["default"]["url"]
            video_url = "https://www.youtube.com/watch?v=" + video_id

            # Get the channel name using the channelId
            channel_response = youtube.channels().list(
                part="snippet",
                id=channel_id
            ).execute()
            channel_name = channel_response["items"][0]["snippet"]["title"]

            videos.append({
                "title": video_title,
                "channelName": channel_name,
                "thumbnail": thumbnail_url,
                "url": video_url
            })

    return videos
