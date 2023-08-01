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

#공식문서 샘플 코드
'''def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options,
    part="id,snippet",
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))

  print("Videos:\n", "\n".join(videos), "\n")

if __name__ == "__main__":
  args = "세종대왕"
  youtube_search(args)'''


from googleapiclient.discovery import build


#채널 이름 제외
'''# 검색어에 해당하는 동영상과 채널을 검색하는 함수를 정의합니다.
def youtube_search(options):
    # YouTube 객체를 생성합니다.
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

    # search.list 메소드를 호출하여 검색 결과를 가져옵니다.
    search_response = youtube.search().list(
        q=options,
        part="id,snippet",
        maxResults=10  # 가져올 검색 결과 개수를 설정합니다.
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        # 검색 결과 중 동영상인 경우에만 처리합니다.
        if search_result["id"]["kind"] == "youtube#video":
            videos.append({
                "title": search_result["snippet"]["title"],
                "thumbnail": search_result["snippet"]["thumbnails"]["default"]["url"],
                "href": "https://www.youtube.com/watch?v=" + search_result["id"]["videoId"]
            })

    # 검색 결과를 출력합니다.
    for video in videos:
        print("제목:", video["title"])
        print("썸네일:", video["thumbnail"])
        print("링크:", video["href"])
        print()


if __name__ == "__main__":
    # 검색어를 입력합니다.
    search_query = "세종대왕"
    youtube_search(search_query)'''


'''def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=options,
    part="id,snippet",
    maxResults=10
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

  print("Videos:")
  for video in videos:
    print("Title:", video["title"])
    print("Channel Name:", video["channelName"])
    print("Thumbnail:", video["thumbnail"])
    print("URL:", video["url"])
    print()


if __name__ == "__main__":
  args = "세종대왕"
  youtube_search(args)'''


'''def youtube_search(options):
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

  print("Videos:")
  for video in videos:
    print("Title:", video["title"])
    print("Channel Name:", video["channelName"])
    print("Thumbnail:", video["thumbnail"])
    print("URL:", video["url"])
    print()


if __name__ == "__main__":
  args = "세종대왕"
  youtube_search(args)'''

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

    return json.dumps(videos, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    args = "세종대왕"
    result = youtube_search(args)
    print(result)
