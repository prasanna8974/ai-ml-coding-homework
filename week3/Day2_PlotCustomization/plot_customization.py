# Week 3 - Tuesday
# Assignment 3: Plot Customization

# Question:
# Create a line chart and customize it using
# figure size, markers, legend, and gridlines.

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [60, 68, 75, 82, 90]

# Set figure size
plt.figure(figsize=(8, 5))

# Create line chart with markers and label
plt.plot(days, marks, marker="o", label="Student Marks")

# Add title and axis labels
plt.title("Student Marks Progress")
plt.xlabel("Day")
plt.ylabel("Marks")

# Add legend
plt.legend()

# Add gridlines
plt.grid()

# Display chart
plt.show()