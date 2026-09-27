# Week 3 - Friday
# Mini EDA Project
# Program 1: Load and Inspect Dataset
#
# Question:
# Read a CSV dataset using Pandas and inspect
# the basic structure of the dataset.

import pandas as pd

# Load CSV file
students = pd.read_csv("student_data.csv")

# Display complete dataset
print("Student Dataset:")
print(students)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(students.head())

# Display number of rows and columns
print("\nDataset Shape:")
print(students.shape)

# Display column names
print("\nColumn Names:")
print(students.columns)

# Display data types
print("\nData Types:")
print(students.dtypes)