# Week 2 - Wednesday
# Assignment 1: Pandas Series Practice
#
# Question:
# Create a Pandas Series.
# Practice indexing, filtering, and accessing values.

import pandas as pd

# Create a Pandas Series
marks = pd.Series([85, 90, 75, 88, 95])

print("Student Marks:")
print(marks)

# Access first value
print("\nFirst Value:")
print(marks[0])

# Access multiple values
print("\nFirst Three Values:")
print(marks[0:3])

# Filter values greater than 80
print("\nMarks Greater Than 80:")
print(marks[marks > 80])