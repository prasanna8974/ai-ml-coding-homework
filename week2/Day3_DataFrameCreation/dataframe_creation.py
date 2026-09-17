# Week 2 - Wednesday
# Assignment 2: DataFrame Creation
#
# Question:
# Create a Pandas DataFrame using a dictionary.
# Display the DataFrame.
# Inspect the rows and columns.

import pandas as pd

# Create student data
student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John"],
    "Age": [26, 24, 25, 23, 27],
    "Marks": [90, 85, 78, 92, 88]
}

# Convert dictionary into DataFrame
students = pd.DataFrame(student_data)

print("Student DataFrame:")
print(students)

# Display first 3 rows
print("\nFirst 3 Rows:")
print(students.head(3))

# Display column names
print("\nColumn Names:")
print(students.columns)

# Display number of rows and columns
print("\nShape:")
print(students.shape)