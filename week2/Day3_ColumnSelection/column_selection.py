# Week 2 - Wednesday
# Assignment 4: Column Selection and Row Filtering
#
# Question:
# Create a Pandas DataFrame.
# Select individual and multiple columns.
# Filter rows based on conditions.

import pandas as pd

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John"],
    "Age": [26, 24, 25, 23, 27],
    "Marks": [90, 85, 78, 92, 88]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

# Select one column
print("\nName Column:")
print(students["Name"])

# Select multiple columns
print("\nName and Marks:")
print(students[["Name", "Marks"]])

# Filter students with marks greater than 85
print("\nStudents with Marks Greater Than 85:")
print(students[students["Marks"] > 85])

# Filter students age 25 or older
print("\nStudents Age 25 or Older:")
print(students[students["Age"] >= 25])