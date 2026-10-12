# Week 6 - Monday
# Assignment 2: K-Means Basics
#
# Question:
# Apply KMeans and print cluster assignments.

from sklearn.cluster import KMeans

# Student study hours and marks
X = [
    [1, 30], [2, 35], [3, 40],
    [7, 75], [8, 85], [9, 90]
]

model = KMeans(n_clusters=2, random_state=42, n_init=10)

clusters = model.fit_predict(X)

print("Cluster Assignments:", clusters)
print("Cluster Centers:")
print(model.cluster_centers_)