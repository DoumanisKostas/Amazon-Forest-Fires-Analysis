import pandas as pd
from googletrans import Translator
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("amazon.csv", thousands='.')
forest_fire_per_month = data.groupby('month')['number'].sum()

# Ensure the month order is correct
months_unique = list(data.month.unique())
forest_fire_per_month = forest_fire_per_month.reindex(months_unique, axis=0)
forest_fire_per_month = forest_fire_per_month.to_frame()
forest_fire_per_month.reset_index(level=0, inplace=True)

# Translate month names to English
translator = Translator()
for i, month in enumerate(forest_fire_per_month['month']):
    translated = translator.translate(month)
    forest_fire_per_month.at[i, 'month'] = translated.text

# Plotting the data
plt.figure(figsize=(25, 15))
plt.bar(forest_fire_per_month['month'], forest_fire_per_month['number'], color=(0.5, 0.1, 0.5, 0.6))
plt.suptitle('Amazon Forest Fires per Month', fontsize=20)
plt.title('Data from 1998 - 2017', fontsize=20)
plt.xlabel('Month', fontsize=20)
plt.ylabel('Number of Fires', fontsize=20)

# Adding text labels
for i, num in enumerate(forest_fire_per_month['number']):
    plt.text(i, num + 10000, num, ha='center', fontsize=15)

# Adjusting label sizes and rotation
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=20)
plt.setp(plt.gca().get_yticklabels(), fontsize=20)

# Save and show the plot
plt.savefig('forest_fires_plot.png')
plt.show()

# Print the dataframe
print(forest_fire_per_month)
