# Week 4 - Monday
# Assignment 3: Feature and Target Identification
#
# Question:
# Create a dataset and identify the
# independent variables (features)
# and dependent variable (target).

import pandas as pd

# Create house dataset
data = {
    "House_Size": [800, 1000, 1200, 1500, 1800],
    "Bedrooms": [1, 2, 2, 3, 4],
    "House_Age": [15, 12, 10, 7, 5],
    "Price": [150000, 190000, 220000, 280000, 350000]
}

houses = pd.DataFrame(data)

print("House Dataset:")
print(houses)


# Independent variables / Features
X = houses[["House_Size", "Bedrooms", "House_Age"]]

# Dependent variable / Target
y = houses["Price"]


print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)


print("\nFeature Columns:")
print(X.columns)

print("\nTarget Column:")
print(y.name)