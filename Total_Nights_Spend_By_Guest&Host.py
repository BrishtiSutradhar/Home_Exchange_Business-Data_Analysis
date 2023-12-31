# -*- coding: utf-8 -*-
"""Final-Project-3-BigQuery bquxjob_27665b8a_18a5fb1d188

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lJ52i-3uKzryu9zYpbeqvgAN0VODj3aB
"""

from google.colab import auth
import pandas as pd
# Will collect your credentials
auth.authenticate_user()

# Query Bigquery
project_id = 'lewagon-final-project-397408'
dataset = 'home_exchange'
table = '408_merged_renew'
query = f'SELECT * FROM {project_id}.{dataset}.{table}'
df4 = pd.read_gbq(query, project_id=project_id)
df4.head(100)

import pandas as pd
df4_cleaned = df4.dropna(subset=['renew'])
df4_cleaned

df4_cleaned['total_nights_sum'] = df4_cleaned['total_nights_guest'] + df4_cleaned['total_nights_host']
df4_cleaned

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
# Assuming your dataframe is named ‘df4_cleaned’
# Create a new column ‘guest_nights_segment’ based on the segmentation criteria
df4_cleaned['guest_nights_segment'] = pd.cut(
    df4_cleaned['total_nights_guest'],
    bins=[0, 10, 31, float('inf')],
    labels=['short', 'medium', 'long'],
    right=False  # Include the left bin edge (0) and exclude the right bin edge (31)
)
# Print the updated dataframe
print(df4_cleaned)

df4_cleaned

segment_avg_renew = df4_cleaned.groupby('guest_nights_segment')['renew'].mean()
# Create a bar plot to visualize the average ‘renew’ values for each segment
segment_avg_renew.plot(kind='bar', figsize=(6, 4))
plt.title('Average Renew by Guest Segment')
plt.xlabel('Guest Segment')
plt.ylabel('Average Renew')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
# Show the plot
plt.tight_layout()
plt.show()

import pandas as pd
# Assuming your dataframe is named ‘df4_cleaned’
# Create a new column ‘guest_nights_segment’ based on the segmentation criteria
df4_cleaned['guest_nights_segment'] = pd.cut(
    df4_cleaned['total_nights_guest'],
    bins=[0, 10, 31, float('inf')],
    labels=['short', 'medium', 'long'],
    right=False  # Include the left bin edge (0) and exclude the right bin edge (31)
)
# Print the updated dataframe
print(df4_cleaned)

import pandas as pd
import matplotlib.pyplot as plt
# Assuming you have a DataFrame called df4_cleaned
# Calculate the average of “total_nights_sum” for each value of “renew”
average_nights_by_renew = df4_cleaned.groupby('renew')['total_nights_sum'].mean()
# Create the bar chart
plt.figure(figsize=(6, 4))
average_nights_by_renew.plot(kind='bar', color='skyblue')
plt.title('Average Total Nights Sum by Renew')
plt.xlabel('Renew (0 or 1)')
plt.ylabel('Average Total Nights Sum')
plt.xticks(rotation=0)
plt.show()
