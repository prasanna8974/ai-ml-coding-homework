# Week 2 - Thursday
# Assignment 4: GroupBy Basics
#
# Question:
# Create a Pandas DataFrame.
# Group the data by Department.
# Calculate student count and average marks
# for each department.

import pandas as pd

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John", "Sam"],
    "Department": ["CS", "IT", "CS", "IT", "CS", "IT"],
    "Marks": [90, 85, 78, 92, 88, 80]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

# Count students in each department
student_count = students.groupby("Department")["Name"].count()

print("\nNumber of Students in Each Department:")
print(student_count)

# Calculate average marks for each department
average_marks = students.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(average_marks)