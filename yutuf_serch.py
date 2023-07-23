import requests
from googleapiclient.discovery import build

def get_youtube_video_ids(api_key, search_query):
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        q=search_query,
        part='id',
        type='video',
        maxResults=15
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]
    return video_ids

if __name__ == "__main__":
    api_key = "AIzaSyASitxw_ki1EAc0jmgipZ77p8Nb0ig4ICc"
    search_query = input("Please enter the query, pănă nutz dau două: ")
    video_ids = get_youtube_video_ids(api_key, search_query)

    if video_ids:
        print("youtube video ids:")
        for video_id in video_ids:
            print(video_id)
    else:
        print("No videos found.")