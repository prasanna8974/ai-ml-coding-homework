# Week 6 - Thursday
# Assignment 1: Anomaly Detection
#
# Question:
# Detect unusual salary values using Z-score.

import numpy as np

salaries = np.array(
    [30000, 32000, 35000, 37000, 40000, 150000]
)

mean = np.mean(salaries)
std = np.std(salaries)

z_scores = (salaries - mean) / std

print("Mean:", mean)
print("Standard Deviation:", std)
print("Z-Scores:", z_scores)

for salary, z in zip(salaries, z_scores):
    if abs(z) > 2:
        print("Outlier:", salary)