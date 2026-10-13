# Week 6 - Tuesday
# Assignment 2: Cluster Label Analysis
#
# Question:
# Group students and analyze each cluster.

import pandas as pd
from sklearn.cluster import KMeans

data = {
    "Study_Hours": [1, 2, 3, 7, 8, 9],
    "Marks": [30, 35, 40, 75, 85, 90]
}

df = pd.DataFrame(data)

model = KMeans(n_clusters=2, random_state=42, n_init=10)

df["Cluster"] = model.fit_predict(df)

print("Student Dataset:")
print(df)

print("\nCluster Averages:")
print(df.groupby("Cluster").mean())