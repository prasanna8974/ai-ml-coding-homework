# Week 2 - Friday
# Assignment 1: Mini Dataset Project
#
# Question:
# Read a student marks dataset.
# Check and clean missing values.
# Create Total and Average columns.
# Analyze the data.
# Display a summary.

import pandas as pd

# Read CSV file
students = pd.read_csv("student_marks.csv")

print("Original Dataset:")
print(students)

# Check missing values
print("\nMissing Values:")
print(students.isnull().sum())

# Fill missing Math marks with the mean
students["Math"] = students["Math"].fillna(
    students["Math"].mean()
)

print("\nCleaned Dataset:")
print(students)

# Create Total column
students["Total"] = students["Math"] + students["Science"]

# Create Average column
students["Average"] = students["Total"] / 2

print("\nDataset After Calculations:")
print(students)

# Overall statistics
print("\nDataset Summary:")
print(students.describe())

# Find student with highest average
highest_student = students.loc[students["Average"].idxmax()]

print("\nStudent With Highest Average:")
print(highest_student["Name"])
print("Average:", highest_student["Average"])

# Department average
print("\nAverage Marks by Department:")
print(students.groupby("Department")["Average"].mean())