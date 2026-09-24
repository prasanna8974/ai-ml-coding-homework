# Week 3 - Thursday
# Assignment 3: Data Type Conversion
#
# Question:
# Practice data type conversion in Pandas.
# 1. Convert strings to numeric values
# 2. Convert strings to dates
# 3. Convert text columns to category type

import pandas as pd

# Create sample dataset
student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya"],
    "Marks": ["90", "85", "78", "92"],
    "Join_Date": ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-25"],
    "Department": ["CS", "IT", "CS", "IT"]
}

students = pd.DataFrame(student_data)

print("Original Data:")
print(students)

print("\nOriginal Data Types:")
print(students.dtypes)


# Convert Marks from string to numeric
students["Marks"] = pd.to_numeric(students["Marks"])


# Convert Join_Date from string to datetime
students["Join_Date"] = pd.to_datetime(students["Join_Date"])


# Convert Department to category
students["Department"] = students["Department"].astype("category")


print("\nData After Conversion:")
print(students)

print("\nNew Data Types:")
print(students.dtypes)