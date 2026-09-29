# Week 4 - Tuesday
# Assignment 1: Linear Regression Basics
#
# Question:
# Create a simple dataset.
# Train a Linear Regression model.
# Generate predictions.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Create dataset
data = {
    "Study_Hours": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10
    ],

    "Marks": [
        42, 48, 53, 59, 65,
        71, 76, 82, 88, 94
    ]
}


# Convert data into DataFrame
students = pd.DataFrame(data)

print("Student Dataset:")
print(students)


# Feature
X = students[["Study_Hours"]]

# Target
y = students["Marks"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Linear Regression model
model = LinearRegression()


# Train model
model.fit(X_train, y_train)


# Make predictions
predictions = model.predict(X_test)


# Display results
print("\nTest Study Hours:")
print(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(predictions)


# Model coefficient
print("\nCoefficient:")
print(model.coef_)


# Model intercept
print("\nIntercept:")
print(model.intercept_)