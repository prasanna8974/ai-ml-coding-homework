# Week 6 - Wednesday
# Assignment 4: Clustering with PCA
#
# Question:
# Apply KMeans on original and PCA-reduced data.
# Compare results and visualize PCA clusters.

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load data
iris = load_iris()
X = iris.data

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans before PCA
model1 = KMeans(n_clusters=3, random_state=42, n_init=10)
labels1 = model1.fit_predict(X_scaled)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# KMeans after PCA
model2 = KMeans(n_clusters=3, random_state=42, n_init=10)
labels2 = model2.fit_predict(X_pca)

# Compare silhouette scores
print("Before PCA:", silhouette_score(X_scaled, labels1))
print("After PCA:", silhouette_score(X_pca, labels2))

# Visualize PCA clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels2, cmap="viridis")

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("KMeans Clustering with PCA")

plt.savefig("pca_clusters.png")
plt.show()