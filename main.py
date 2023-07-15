import configparser
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googleapiclient.discovery import build
import pandas as pd

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['api-key']['api_key']

service = build('youtube', 'v3', developerKey=api_key)

video_id = 'tdZX2GdByS8'

comments = []

results = service.commentThreads().list(
    part='snippet',
    videoId=video_id,
    textFormat='plainText',
).execute()

while results:
    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    if 'nextPageToken' in results:
        results = service.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=results['nextPageToken']
        ).execute()
    else:
        break

df = pd.DataFrame(comments, columns=['comments'])
df.to_csv('output.csv', index=False)

for com in comments:
    print(sid.polarity_scores(com))

service.close()