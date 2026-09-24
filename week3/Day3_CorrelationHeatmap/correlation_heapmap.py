# Week 3 - Wednesday
# Assignment 3: Correlation Heatmap
#
# Question:
# Create a correlation matrix for numerical data
# and visualize the correlations using a heatmap.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create sample student dataset
student_data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7],
    "Attendance": [60, 65, 70, 75, 80, 90, 95],
    "Marks": [50, 55, 65, 70, 78, 85, 92]
}

students = pd.DataFrame(student_data)

print("Student Data:")
print(students)

# Calculate correlation matrix
correlation = students.corr()

print("\nCorrelation Matrix:")
print(correlation)

# Create heatmap
sns.heatmap(correlation, annot=True)

plt.title("Student Data Correlation Heatmap")

plt.show()