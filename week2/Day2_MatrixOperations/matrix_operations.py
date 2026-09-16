# Week 2 - Tuesday
# Assignment 4: Matrix Operations
#
# Question:
# Create two matrices using NumPy.
# Perform matrix addition.
# Perform element-wise multiplication.
# Perform matrix multiplication.

import numpy as np

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix addition
addition = matrix1 + matrix2

print("\nMatrix Addition:")
print(addition)

# Element-wise multiplication
element_multiplication = matrix1 * matrix2

print("\nElement-wise Multiplication:")
print(element_multiplication)

# Matrix multiplication
matrix_multiplication = np.dot(matrix1, matrix2)

print("\nMatrix Multiplication:")
print(matrix_multiplication)