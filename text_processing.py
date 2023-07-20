import os.path
import pandas as pd
import re
import datetime
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import pipeline

model_id = 'siebert/sentiment-roberta-large-english'

sentiment_pipeline = pipeline('sentiment-analysis',model=model_id)

lemmatizer = WordNetLemmatizer()

# nltk.download('all') only downloading when first create the project

data = pd.read_csv('output.csv', encoding='latin-1')

text = list(data['comments'])

corpus = []

for i in range(len(text)):
    r = re.sub('^a-zA-Z]', ' ', text[i])
    r = r.lower()
    r = r.split()
    r = [word for word in r if word not in stopwords.words('english')]
    r = [lemmatizer.lemmatize(word) for word in r]
    r = ' '.join(r)
    corpus.append(r)

data['comments'] = corpus

sentiment_res = []

for comments in corpus:
    sentiment_res.append(sentiment_pipeline(comments))

file_path = 'result.csv'

file_exists = os.path.exists(file_path)

with open('result.csv', 'a', encoding='utf-8') as f:
    if not file_exists:
        f.write("video_id,date created,comment,result,score\n")

    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    for index in range(len(sentiment_res)):
        f.write("{0},\"{1}\",{2},{3}".format(
                                    time_string,
                                    corpus[index],
                                    sentiment_res[index][0]['label'],
                                    sentiment_res[index][0]['score']))
        f.write('\n')