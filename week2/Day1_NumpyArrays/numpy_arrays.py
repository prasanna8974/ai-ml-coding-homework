# Week 2 - Day 1
# Assignment: NumPy Array Creation
#
# Question:
# 1. Create a 1D NumPy array.
# 2. Create a 2D NumPy array.
# 3. Print each array.
# 4. Check the shape, size, and number of dimensions.

import numpy as np


# Create a 1D array
array_1d = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(array_1d)

print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Dimensions:", array_1d.ndim)


print("--------------------")


# Create a 2D array
array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("2D Array:")
print(array_2d)

print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Dimensions:", array_2d.ndim)