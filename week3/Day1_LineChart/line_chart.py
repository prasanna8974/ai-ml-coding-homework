# Week 3 - Monday
# Assignment 2: Matplotlib Basics - Line Chart
#
# Question:
# Create a simple line chart using Matplotlib.
# Add a title and axis labels.

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [60, 70, 75, 85, 90]

plt.plot(days, marks)

plt.title("Student Marks Progress")
plt.xlabel("Day")
plt.ylabel("Marks")

plt.show()