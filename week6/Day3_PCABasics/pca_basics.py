# Week 6 - Wednesday
# Assignment 1: PCA Basics
#
# Question:
# Reduce 3 features into 2 principal components.

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Dataset: Study Hours, Attendance, Marks
X = [
    [1, 40, 30],
    [2, 50, 40],
    [3, 60, 50],
    [7, 80, 75],
    [8, 90, 85],
    [9, 95, 90]
]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Original Data:")
print(X)

print("\nData After PCA:")
print(X_pca)

print("\nOriginal Shape:", scaler.n_features_in_)
print("Reduced Shape:", X_pca.shape)