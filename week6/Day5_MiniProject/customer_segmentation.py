# Week 6 - Friday
# Assignment 1: Customer Segmentation Mini Project
#
# Question:
# Build a customer segmentation model using KMeans.
# Clean data, scale features, find clusters and visualize.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Step 1: Create customer dataset
data = {
    "CustomerID": list(range(1, 21)),
    "AnnualIncome": [
        30000, 35000, 32000, 38000, 40000,
        45000, 48000, 50000, 52000, 55000,
        65000, 68000, 70000, 75000, 78000,
        85000, 88000, 90000, 95000, 100000
    ],
    "SpendingScore": [
        20, 25, 22, 30, 35,
        40, 45, 48, 50, 55,
        60, 62, 65, 70, 72,
        80, 82, 85, 90, 95
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates and missing values
df = df.drop_duplicates()
df = df.dropna()

# Step 3: Select features
X = df[["AnnualIncome", "SpendingScore"]]

# Step 4: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Elbow Method
inertia = []

for k in range(1, 7):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    model.fit(X_scaled)
    inertia.append(model.inertia_)

plt.figure()
plt.plot(range(1, 7), inertia, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.savefig("elbow_method.png")
plt.close()

# Step 6: KMeans clustering
# Use 3 clusters as an initial project choice
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nCustomer Clusters:")
print(df)

# Step 7: Analyze clusters
print("\nCluster Summary:")
print(
    df.groupby("Cluster")[
        ["AnnualIncome", "SpendingScore"]
    ].mean()
)

# Step 8: Evaluate clustering
score = silhouette_score(
    X_scaled,
    df["Cluster"]
)

print("\nSilhouette Score:", round(score, 3))

# Step 9: PCA visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure()
plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=df["Cluster"],
    cmap="viridis"
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Customer Segmentation Using PCA")
plt.savefig("customer_clusters.png")
plt.close()

# Step 10: Save final dataset
df.to_csv("customer_segments.csv", index=False)

print("\nProject completed successfully!")