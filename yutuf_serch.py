import configurator
import validators

# Configuration of YT API
cfg = configurator.Configurator()


# https://www.youtube.com/watch?v=video_id for testing the video id source

def get_youtube_video_ids(search_yt_query):
    search_response = cfg.service.search().list(
        q=search_yt_query,
        part='id',
        type='video',
        maxResults=5
    ).execute()

    video_yt_ids = [item['id']['videoId'] for item in search_response['items']]
    return video_yt_ids


search_yt_query = input("Please enter the query : ").lower()
video_ids = get_youtube_video_ids(search_yt_query)
if video_ids:
    print("youtube video ids:")
    for video_id in video_ids:
        validation = validators.url("https://www.youtube.com/watch?v={0}".format(video_id))
        if validation:
            print(video_id)
        else:
            print("Invalid URL")

else:
    print("No videos found.")
