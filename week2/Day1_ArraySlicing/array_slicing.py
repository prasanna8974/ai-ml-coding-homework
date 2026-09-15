# Week 2 - Day 1
# Assignment : Array Indexing and Slicing
#
# Question:
# Create a 2D NumPy array.
# Access individual elements, rows, and columns.
# Practice array slicing.

import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Array:")
print(numbers)

print("First element:", numbers[0, 0])

print("Second row:", numbers[1])

print("First column:", numbers[:, 0])

print("First two rows:")
print(numbers[0:2])

print("First two columns:")
print(numbers[:, 0:2])
