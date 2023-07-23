# dan implementation for data visualization

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result.csv', sep=';')

sentiment_counts = data['result'].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['blue', 'red'])

for i, count in enumerate(sentiment_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Count of Positive and Negative Sentiments')

plt.show()
