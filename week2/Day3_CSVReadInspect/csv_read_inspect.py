# Week 2 - Wednesday
# Assignment 3: CSV Read and Inspect
#
# Question:
# Read a CSV file using Pandas.
# Inspect the dataset using head(), tail(), info(), and describe().

import pandas as pd

# Read CSV file
students = pd.read_csv("students.csv")

print("Student Dataset:")
print(students)

# First 5 rows
print("\nFirst 5 Rows:")
print(students.head())

# Last 5 rows
print("\nLast 5 Rows:")
print(students.tail())

# Dataset information
print("\nDataset Information:")
students.info()

# Statistical summary
print("\nStatistical Summary:")
print(students.describe())