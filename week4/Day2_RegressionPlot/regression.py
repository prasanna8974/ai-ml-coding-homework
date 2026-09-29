# Week 4 - Tuesday
# Assignment 2: Regression Visualization
#
# Question:
# Train a Linear Regression model.
# Compare actual and predicted values using a graph.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Create dataset
data = {
    "Experience": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10
    ],

    "Salary": [
        40000, 45000, 50000, 56000, 61000,
        67000, 72000, 78000, 84000, 90000
    ]
}

employees = pd.DataFrame(data)

print("Employee Dataset:")
print(employees)


# Feature
X = employees[["Experience"]]

# Target
y = employees["Salary"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LinearRegression()


# Train model
model.fit(X_train, y_train)


# Make predictions
predictions = model.predict(X_test)


# Display actual and predicted values
print("\nActual Salary:")
print(y_test.values)

print("\nPredicted Salary:")
print(predictions)


# Plot actual values
plt.scatter(
    X_test["Experience"],
    y_test,
    label="Actual Salary"
)


# Plot predicted values
plt.scatter(
    X_test["Experience"],
    predictions,
    label="Predicted Salary"
)


# Regression line
plt.plot(
    employees["Experience"],
    model.predict(employees[["Experience"]]),
    label="Regression Line"
)


plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.legend()
plt.grid()

plt.show()