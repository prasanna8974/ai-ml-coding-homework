# Week 6 - Wednesday
# Assignment 3: Explained Variance
#
# Question:
# Calculate explained variance of PCA components.

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
pca.fit(X_scaled)

print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Variance Preserved:")
print(sum(pca.explained_variance_ratio_) * 100, "%")