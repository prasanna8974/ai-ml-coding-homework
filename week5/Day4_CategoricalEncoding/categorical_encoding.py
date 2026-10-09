# Week 5 - Thursday
# Assignment 2: Categorical Encoding
#
# Question:
# Apply Label Encoding and One-Hot Encoding.

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create dataset
data = {
    "Employee": ["A", "B", "C", "D", "E"],
    "Department": ["IT", "HR", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Label Encoding
encoder = LabelEncoder()
df["Label_Encoded"] = encoder.fit_transform(
    df["Department"]
)

print("\nLabel Encoded Data:")
print(df)

# One-Hot Encoding
one_hot = pd.get_dummies(
    df["Department"],
    dtype=int
)

print("\nOne-Hot Encoded Data:")
print(one_hot)