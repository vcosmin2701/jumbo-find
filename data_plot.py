# dan implementation for bar plotting

import pandas as pd
from matplotlib import pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('result.csv', header=None)

# Extract the data from column 2 (index 1 in pandas, as indexing starts from 0)
t = df[2]

# Count the occurrences of each category
counts = t.value_counts()

# Create a plot with two bars, one for positive and one for negative values
plt.figure(figsize=(7, 5))  # Adjust the size of the plot as per your preference

# Plot positive values in blue
plt.bar('POSITIVE', counts['POSITIVE'], color='blue', label='POSITIVE')
plt.text('POSITIVE', counts['POSITIVE'], str(counts['POSITIVE']), ha='center', va='bottom')
# Plot negative values in red
plt.bar('NEGATIVE', counts['NEGATIVE'], color='red', label='NEGATIVE')
plt.text('NEGATIVE', counts['NEGATIVE'], str(counts['NEGATIVE']), ha='center', va='bottom')

# Optionally, add labels and a legend
plt.xlabel('Category')
plt.ylabel('Count')
plt.legend()

# Show the plot
plt.show()
