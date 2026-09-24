# Week 3 - Thursday
# Assignment 2: Outlier Detection Basics
#
# Question:
# Detect outliers using the IQR method
# and visualize the data using a box plot.

import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
marks = [65, 70, 72, 75, 78, 80, 82, 85, 88, 90, 150]

students = pd.DataFrame({
    "Marks": marks
})

print("Student Marks:")
print(students)

# Calculate Q1 and Q3
Q1 = students["Marks"].quantile(0.25)
Q3 = students["Marks"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

# Calculate lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Find outliers
outliers = students[
    (students["Marks"] < lower_limit) |
    (students["Marks"] > upper_limit)
]

print("\nOutliers:")
print(outliers)

# Create box plot
plt.boxplot(students["Marks"])

plt.title("Student Marks - Outlier Detection")
plt.ylabel("Marks")

plt.show()