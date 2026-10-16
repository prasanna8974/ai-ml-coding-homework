# Week 6 - Thursday
# Assignment 3: Real Data Outlier Handling
#
# Question:
# Detect outliers using IQR and remove them.

import pandas as pd

data = {
    "Salary": [
        30000, 32000, 35000,
        37000, 40000, 42000, 150000
    ]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nOriginal Average:", df["Salary"].mean())

# Calculate IQR
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Remove outliers
clean_df = df[
    (df["Salary"] >= lower) &
    (df["Salary"] <= upper)
]

print("\nCleaned Data:")
print(clean_df)

print("\nCleaned Average:", clean_df["Salary"].mean())