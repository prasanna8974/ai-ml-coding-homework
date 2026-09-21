# Week 3 - Monday
# Assignment 1: NumPy and Pandas Test
#
# Topics:
# 1. NumPy Arrays
# 2. Basic Statistics
# 3. Pandas DataFrame
# 4. DataFrame Filtering

import numpy as np
import pandas as pd


# Question 1: NumPy Array

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Shape:", numbers.shape)


# Question 2: Basic Statistics

print("\nBasic Statistics:")
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))


# Question 3: Pandas DataFrame

student_data = {
    "Name": ["Prasanna", "Anu", "Ravi", "Priya", "John"],
    "Marks": [90, 75, 82, 95, 68]
}

students = pd.DataFrame(student_data)

print("\nStudent DataFrame:")
print(students)


# Question 4: DataFrame Filtering

print("\nStudents With Marks Greater Than 80:")
print(students[students["Marks"] > 80])