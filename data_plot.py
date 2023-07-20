# dan implementation for bar plotting

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('result.csv', header=None)

t = df[2]

counts = t.value_counts()

plt.figure(figsize=(7, 5))

plt.bar('POSITIVE', counts['POSITIVE'], color='blue', label='POSITIVE')
plt.text('POSITIVE', counts['POSITIVE'], str(counts['POSITIVE']), ha='center', va='bottom')

plt.bar('NEGATIVE', counts['NEGATIVE'], color='red', label='NEGATIVE')
plt.text('NEGATIVE', counts['NEGATIVE'], str(counts['NEGATIVE']), ha='center', va='bottom')

plt.xlabel('Category')
plt.ylabel('Count')
plt.legend()

plt.show()
