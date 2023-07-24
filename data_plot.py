import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('result.csv', sep=';')

sentiment_counts = data['result'].value_counts()

plt.figure(figsize=(6, 5))
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['blue', 'red'])

for i, count in enumerate(sentiment_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Count of Positive and Negative Sentiments for entire dataset')
dataset_file = f"./plots/entire_dataset.png"
plt.savefig(dataset_file, bbox_inches='tight')
plt.show()

data_group = data.groupby('id')

for group_id, group_df in data_group:
    sentiment_counts = group_df['result'].value_counts()
    plt.figure(figsize=(6, 4))
    plt.bar(sentiment_counts.index, sentiment_counts.values)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title(f'Sentiment Distribution for ID: {group_id}')
    plt.xticks(rotation=45)

    for i, count in enumerate(sentiment_counts.values):
        plt.text(i, count, str(count), ha='center', va='bottom')

    filename = f'plots/sentiment_distribution_{group_id}.png'
    plt.savefig(filename, bbox_inches='tight')

plt.show()
