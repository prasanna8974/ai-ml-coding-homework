# Week 3 - Thursday
# Assignment 4: EDA Summary
#
# Question:
# Perform basic Exploratory Data Analysis (EDA)
# and write five observations with charts.

import pandas as pd
import matplotlib.pyplot as plt

# Create sample dataset
student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John", "Sam"],
    "Department": ["CS", "IT", "CS", "IT", "CS", "IT"],
    "Study_Hours": [6, 4, 5, 7, 3, 4],
    "Marks": [90, 75, 82, 95, 68, 78]
}

students = pd.DataFrame(student_data)

# Display dataset
print("Student Dataset:")
print(students)

# Basic information
print("\nDataset Information:")
students.info()

# Basic statistics
print("\nStatistical Summary:")
print(students.describe())

# Check missing values
print("\nMissing Values:")
print(students.isnull().sum())

# Observation 1
print("\nObservation 1:")
print("Average Marks:", students["Marks"].mean())

# Observation 2
print("\nObservation 2:")
print("Highest Marks:", students["Marks"].max())

# Observation 3
print("\nObservation 3:")
print("Lowest Marks:", students["Marks"].min())

# Observation 4
print("\nObservation 4:")
print("Average Marks by Department:")
print(students.groupby("Department")["Marks"].mean())

# Observation 5
print("\nObservation 5:")
print("Students with Marks Greater Than 80:")
print(students[students["Marks"] > 80])

# Chart 1 - Marks by Student
plt.bar(students["Name"], students["Marks"])

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()

# Chart 2 - Study Hours vs Marks
plt.scatter(students["Study_Hours"], students["Marks"])

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()