# Week 2 - Thursday
# Assignment 2: Sorting and Renaming
#
# Question:
# Create a Pandas DataFrame.
# Rename a column.
# Sort the records based on Marks.

import pandas as pd

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John"],
    "Age": [26, 24, 25, 23, 27],
    "Marks": [90, 85, 78, 92, 88]
}

students = pd.DataFrame(student_data)

print("Original DataFrame:")
print(students)

# Rename Marks column to Score
students = students.rename(columns={"Marks": "Score"})

print("\nAfter Renaming Column:")
print(students)

# Sort by Score from lowest to highest
sorted_students = students.sort_values(by="Score")

print("\nSorted by Score - Ascending:")
print(sorted_students)

# Sort by Score from highest to lowest
sorted_descending = students.sort_values(
    by="Score",
    ascending=False
)

print("\nSorted by Score - Descending:")
print(sorted_descending)