# Week 2 - Friday
# Assignment 2: Week 2 Summary
#
# Topics Covered:
# NumPy Arrays
# Array Indexing and Slicing
# Array Math
# Reshape and Flatten
# Random Arrays
# Statistics
# Matrix Operations
# Pandas Series
# Pandas DataFrames
# CSV Files
# Missing Values
# Sorting
# New Columns
# GroupBy


# -------------------------
# NUMPY SUMMARY
# -------------------------

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(numbers)

print("\nMean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))


# -------------------------
# PANDAS SUMMARY
# -------------------------

import pandas as pd

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi"],
    "Department": ["CS", "IT", "CS"],
    "Marks": [90, 85, 78]
}

students = pd.DataFrame(student_data)

print("\nPandas DataFrame:")
print(students)

print("\nStudents With Marks Greater Than 80:")
print(students[students["Marks"] > 80])

print("\nAverage Marks by Department:")
print(students.groupby("Department")["Marks"].mean())