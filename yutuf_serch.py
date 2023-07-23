import configurator

# Configuration of YT API
cfg = configurator.Configurator()

# https://www.youtube.com/watch?v=video_id for testing the video id source

def get_youtube_video_ids(search_query):
    search_response = cfg.service.search().list(
        q=search_query,
        part='id',
        type='video',
        maxResults=15
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]
    return video_ids


if __name__ == "__main__":
    search_query = input("Please enter the query : ")
    video_ids = get_youtube_video_ids(search_query)

    if video_ids:
        print("youtube video ids:")
        for video_id in video_ids:
            print(video_id)
    else:
        print("No videos found.")
