# Week 6 - Thursday
# Assignment 2: Distance-Based Outlier Check
#
# Question:
# Find an unusual data point using distance.

import numpy as np

X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [20, 25]
])

# Calculate the center
center = np.mean(X, axis=0)

# Calculate distance from center
distances = np.linalg.norm(X - center, axis=1)

print("Center:", center)
print("Distances:", distances)

# Find the farthest point
outlier_index = np.argmax(distances)

print("Most Distant Point:", X[outlier_index])