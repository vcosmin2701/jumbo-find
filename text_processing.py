import nltk
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

nltk.download('all')

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
print(data.head())