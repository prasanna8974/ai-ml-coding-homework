# Week 3 - Wednesday
# Assignment 2: Distribution Analysis
#
# Question:
# Analyze the distribution of student marks.
# Calculate mean and median.
# Create a histogram to visualize the distribution.

import pandas as pd
import matplotlib.pyplot as plt

marks = [65, 70, 72, 75, 78, 80, 82, 85, 88, 90, 95]

students = pd.DataFrame({
    "Marks": marks
})

print("Student Marks:")
print(students)

# Calculate mean
mean_marks = students["Marks"].mean()

# Calculate median
median_marks = students["Marks"].median()

print("\nMean:", mean_marks)
print("Median:", median_marks)

# Create histogram
plt.hist(students["Marks"], bins=5)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()