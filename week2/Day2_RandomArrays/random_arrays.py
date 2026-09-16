# Week 2 - Tuesday
# Assignment 2: Random Number Arrays
#
# Question:
# Generate random integers and random decimal numbers using NumPy.
# Print the generated arrays.
# Check the minimum and maximum values.

import numpy as np

# Generate 5 random integers from 1 to 100
random_integers = np.random.randint(1, 101, 5)

print("Random Integers:")
print(random_integers)

print("Minimum:", random_integers.min())
print("Maximum:", random_integers.max())


# Generate 5 random decimal numbers between 0 and 1
random_floats = np.random.random(5)

print("\nRandom Floats:")
print(random_floats)

print("Minimum:", random_floats.min())
print("Maximum:", random_floats.max())