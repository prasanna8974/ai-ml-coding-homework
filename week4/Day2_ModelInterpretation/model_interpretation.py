# Week 4 - Tuesday
# Assignment 4: Model Interpretation
#
# Question:
# Train a Linear Regression model and explain
# the coefficient, intercept, predictions,
# and model behavior.

import pandas as pd
from sklearn.linear_model import LinearRegression


# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [45, 50, 56, 61, 67, 72, 78, 84]
}

students = pd.DataFrame(data)

print("Student Dataset:")
print(students)


# Feature
X = students[["Study_Hours"]]

# Target
y = students["Marks"]


# Create model
model = LinearRegression()


# Train model
model.fit(X, y)


# Get coefficient
coefficient = model.coef_[0]


# Get intercept
intercept = model.intercept_


print("\nCoefficient:")
print(coefficient)

print("\nIntercept:")
print(intercept)


# Predict marks for 9 study hours
new_data = pd.DataFrame({
    "Study_Hours": [9]
})

prediction = model.predict(new_data)

print("\nPredicted Marks for 9 Study Hours:")
print(prediction[0])


# Model Interpretation
print("\nMODEL INTERPRETATION:")

print(
    "1. The coefficient shows how much the predicted "
    "marks change when study hours increase by one hour."
)

print(
    "2. The intercept is the model's predicted value "
    "when Study_Hours is zero."
)

print(
    "3. The model uses the relationship between "
    "Study_Hours and Marks to make predictions."
)

print(
    "4. A positive coefficient means predicted marks "
    "increase as study hours increase."
)

print(
    "5. Linear Regression assumes an approximately "
    "linear relationship between the feature and target."
)