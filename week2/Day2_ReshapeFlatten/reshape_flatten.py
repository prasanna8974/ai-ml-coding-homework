# Week 2 - Tuesday
# Assignment 1: Reshape and Flatten
#
# Question:
# Create a NumPy array with 6 numbers.
# Reshape the array into 2 rows and 3 columns.
# Flatten the 2D array back into a 1D array.
# Print the shape after each operation.

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(numbers)
print("Shape:", numbers.shape)

# Reshape into 2 rows and 3 columns
reshaped_array = numbers.reshape(2, 3)

print("\nReshaped Array:")
print(reshaped_array)
print("Shape:", reshaped_array.shape)

# Flatten back into one dimension
flattened_array = reshaped_array.flatten()

print("\nFlattened Array:")
print(flattened_array)
print("Shape:", flattened_array.shape)