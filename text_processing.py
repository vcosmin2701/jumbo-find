# import nltk
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import pipeline

sentiment_pipeline = pipeline('sentiment-analysis')

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

for index in range(len(sentiment_res)):
    print(" \n Comment: {0} \n Result: {1} \n Score: {2}".format(corpus[index],
                                                                sentiment_res[index][0]['label'],
                                                                sentiment_res[index][0]['score']))

df = pd.DataFrame(text)