# Week 2 - Tuesday
# Assignment 3: Mean, Median and Standard Deviation
#
# Question:
# Create a NumPy array.
# Calculate the mean, median, and standard deviation.
# Also calculate the mean manually and compare the results.

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Numbers:", numbers)

# Using NumPy
mean = np.mean(numbers)
median = np.median(numbers)
standard_deviation = np.std(numbers)

print("\nUsing NumPy:")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", standard_deviation)

# Calculate mean manually
total = 0

for number in numbers:
    total += number

manual_mean = total / len(numbers)

print("\nManual Calculation:")
print("Manual Mean:", manual_mean)