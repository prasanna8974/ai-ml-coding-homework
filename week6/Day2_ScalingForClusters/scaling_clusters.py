# Week 6 - Tuesday
# Assignment 3: Scaling Before Clustering
#
# Question:
# Compare KMeans before and after scaling.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [20, 21, 22, 45, 46, 47],
    "Salary": [20000, 80000, 21000, 79000, 22000, 81000]
}

df = pd.DataFrame(data)

# Before scaling
model1 = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Before_Scaling"] = model1.fit_predict(df)

# After scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[["Age", "Salary"]])

model2 = KMeans(n_clusters=2, random_state=42, n_init=10)
df["After_Scaling"] = model2.fit_predict(X_scaled)

print(df)