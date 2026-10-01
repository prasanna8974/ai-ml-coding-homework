# Week 4 - Wednesday
# Assignment 1: Logistic Regression Basics
#
# Question:
# Create a binary classification dataset.
# Train a Logistic Regression model.
# Predict whether a student will Pass or Fail.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Create dataset
data = {
    "Study_Hours": [
        1, 2, 2, 3, 3,
        4, 5, 6, 7, 8,
        9, 10
    ],

    "Attendance": [
        50, 55, 60, 62, 65,
        70, 75, 80, 85, 88,
        92, 95
    ],

    "Pass": [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        1, 1
    ]
}


# Convert into DataFrame
students = pd.DataFrame(data)

print("Student Dataset:")
print(students)


# Features
X = students[
    ["Study_Hours", "Attendance"]
]


# Target
y = students["Pass"]


print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# Create Logistic Regression model
model = LogisticRegression()


# Train model
model.fit(
    X_train,
    y_train
)


# Make predictions
predictions = model.predict(X_test)


print("\nActual Results:")
print(y_test.values)

print("\nPredicted Results:")
print(predictions)