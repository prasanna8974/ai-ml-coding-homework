# Week 3 - Thursday
# Assignment 1: Data Cleaning Practice
#
# Question:
# Create a sample dataset and perform data cleaning.
# 1. Check duplicate rows
# 2. Remove duplicate rows
# 3. Standardize text values

import pandas as pd

# Create sample data
student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Prasanna", "Priya"],
    "Department": ["CS", "it", "CS", "CS", "IT"],
    "Marks": [90, 85, 78, 90, 92]
}

students = pd.DataFrame(student_data)

print("Original Data:")
print(students)


# Check duplicate rows
print("\nDuplicate Rows:")
print(students.duplicated())


# Remove duplicate rows
students = students.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(students)


# Standardize Department values
students["Department"] = students["Department"].str.upper()

print("\nAfter Standardizing Department:")
print(students)