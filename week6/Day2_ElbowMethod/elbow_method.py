# Week 6 - Tuesday
# Assignment 1: Elbow Method
#
# Question:
# Find a suitable number of clusters using KMeans.

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = [
    [1, 20], [2, 25], [3, 30],
    [7, 70], [8, 75], [9, 80],
    [13, 120], [14, 125], [15, 130]
]

inertia = []

for k in range(1, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertia.append(model.inertia_)

plt.plot(range(1, 7), inertia, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.savefig("elbow_plot.png")
plt.show()