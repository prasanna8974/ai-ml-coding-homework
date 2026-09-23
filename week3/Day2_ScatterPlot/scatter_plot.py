# Week 3 - Tuesday
# Assignment 1: Scatter Plot
#
# Question:
# Plot two numerical variables using a scatter plot
# and observe the relationship between them.

import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7]
marks = [50, 55, 65, 70, 78, 85, 92]

plt.scatter(study_hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()