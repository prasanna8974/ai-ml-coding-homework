# Week 4 - Thursday
# Assignment 2: Feature Scaling Basics
#
# Question:
# Create a dataset and apply
# StandardScaler and MinMaxScaler.
# Compare the original and scaled data.

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


# Create dataset
data = {
    "Age": [
        22, 25, 30, 35, 40,
        45, 50, 55
    ],

    "Salary": [
        30000, 35000, 45000, 55000,
        65000, 75000, 85000, 100000
    ]
}


# Create DataFrame
employees = pd.DataFrame(data)


print("ORIGINAL DATA:")
print(employees)


# -----------------------------
# StandardScaler
# -----------------------------

standard_scaler = StandardScaler()

standard_scaled = standard_scaler.fit_transform(
    employees
)


standard_df = pd.DataFrame(
    standard_scaled,
    columns=["Age", "Salary"]
)


print("\nSTANDARD SCALED DATA:")
print(standard_df)


# -----------------------------
# MinMaxScaler
# -----------------------------

minmax_scaler = MinMaxScaler()

minmax_scaled = minmax_scaler.fit_transform(
    employees
)


minmax_df = pd.DataFrame(
    minmax_scaled,
    columns=["Age", "Salary"]
)


print("\nMIN-MAX SCALED DATA:")
print(minmax_df)