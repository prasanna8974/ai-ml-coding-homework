# Week 6 - Tuesday
# Assignment 4: Customer Clustering
#
# Question:
# Group customers based on income and spending.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Customer": ["A", "B", "C", "D", "E", "F"],
    "Income": [25000, 30000, 35000, 70000, 80000, 90000],
    "Spending": [20, 25, 30, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Income", "Spending"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=2, random_state=42, n_init=10)

df["Cluster"] = model.fit_predict(X_scaled)

print("Customer Segmentation:")
print(df)

print("\nCluster Averages:")
print(df.groupby("Cluster")[["Income", "Spending"]].mean())