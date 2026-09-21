# Week 3 - Monday
# Assignment 4: Histogram Plot
#
# Question:
# Create a histogram using sample numeric data
# and experiment with bins.

import matplotlib.pyplot as plt

marks = [45, 55, 60, 62, 65, 68, 70, 72, 75, 78,
         80, 82, 85, 88, 90, 92, 95]

plt.hist(marks, bins=5)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()