# Week 2 - Thursday
# Assignment 1: Missing Values Basics
#
# Question:
# Create a DataFrame with missing values.
# Identify missing values.
# Fill missing values.
# Drop rows containing missing values.

import pandas as pd
import numpy as np

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John"],
    "Age": [26, 24, np.nan, 23, 27],
    "Marks": [90, np.nan, 78, 92, 88]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

# Identify missing values
print("\nMissing Values:")
print(students.isnull())

# Count missing values
print("\nMissing Value Count:")
print(students.isnull().sum())

# Fill missing values
filled_students = students.fillna(0)

print("\nAfter Filling Missing Values:")
print(filled_students)

# Drop rows containing missing values
dropped_students = students.dropna()

print("\nAfter Dropping Missing Values:")
print(dropped_students)