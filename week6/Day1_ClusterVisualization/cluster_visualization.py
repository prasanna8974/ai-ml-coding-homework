# Week 6 - Monday
# Assignment 3: Cluster Visualization
#
# Question:
# Visualize student groups using a scatter plot.

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

hours = [1, 2, 3, 7, 8, 9]
marks = [30, 35, 40, 75, 85, 90]

X = list(zip(hours, marks))

model = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters = model.fit_predict(X)

plt.scatter(hours, marks, c=clusters, cmap="viridis")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Clusters")

plt.savefig("student_clusters.png")
plt.show()