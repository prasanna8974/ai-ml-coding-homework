# Week 2 - Thursday
# Assignment 3: New Column Creation
#
# Question:
# Create a Pandas DataFrame.
# Create new columns using calculations
# from existing columns.

import pandas as pd

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John"],
    "Math": [90, 85, 78, 92, 88],
    "Science": [85, 80, 82, 90, 86]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

# Create Total column
students["Total"] = students["Math"] + students["Science"]

# Create Average column
students["Average"] = students["Total"] / 2

print("\nDataFrame After Creating New Columns:")
print(students)