import configurator
import validators
from datetime import datetime

# Configuration of YT API
cfg = configurator.Configurator()


# https://www.youtube.com/watch?v=video_id for testing the video id source

def get_published_date_for_video(video_id):
    video_response = cfg.service.videos().list(
        part='snippet',
        id=video_id
    ).execute()
    published_date = video_response['items'][0]['snippet']['publishedAt']
    return published_date


def get_youtube_video_ids(search_yt_query):
    search_response = cfg.service.search().list(
        q=search_yt_query,
        part='id',
        type='video',
        maxResults=15
    ).execute()

    video_yt_ids = [item['id']['videoId'] for item in search_response['items']]

    video_info_list = []
    for video_id in video_yt_ids:
        validation = validators.url("https://www.youtube.com/watch?v={0}".format(video_id))
        if validation:
            published_date = get_published_date_for_video(video_id)
            video_info_list.append((video_id, published_date))
        else:
            print("Invalid URL for video ID:", video_id)

    return video_info_list


def print_url_video(yt_video_id):
    url = "https://www.youtube.com/watch?v={0}".format(yt_video_id)
    return url


search_yt_query = input("Please enter the query: ").lower()
video_info_list = get_youtube_video_ids(search_yt_query)

if video_info_list:
    print("YouTube IDs and Date:")
    for video_info in video_info_list:
        video_id = video_info[0]
        published_date = video_info[1]
        formatted_date = datetime.fromisoformat(published_date.replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S')
        print("ID: {0} Published Date: {1} URL: {2}".format(video_id, formatted_date, print_url_video(video_id)))
else:
    print("No videos found.")
