import configurator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

# nltk.download('vader_lexicon')
# video_id = 'tdZX2GdByS8' test

# Configuration of YT API
cfg = configurator.Configurator()

sid = SentimentIntensityAnalyzer()

video_id = input('Input video id: ')
if len(video_id) > 11:
    raise Exception("Invalid video id, please check again the id")

id = video_id

comments = []

results = cfg.service.commentThreads().list(
    part='snippet',
    videoId=video_id,
    textFormat='plainText',
).execute()

while results:
    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    if 'nextPageToken' in results:
        results = cfg.service.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=results['nextPageToken']
        ).execute()
    else:
        break

df = pd.DataFrame(comments, columns=['comments'])
df.to_csv('output.csv', index=False)

cfg.service.close()

exec(open("text_processing.py").read())


