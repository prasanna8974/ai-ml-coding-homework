# Week 4 - Monday
# Assignment 4: Scikit-learn Basics Setup
#
# Question:
# Create a basic machine learning workflow using
# fit(), predict(), and model evaluation.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [42, 48, 53, 60, 65, 71, 77, 83, 89, 94]
}

students = pd.DataFrame(data)

print("Student Dataset:")
print(students)


# Step 1: Features and Target
X = students[["Study_Hours"]]
y = students["Marks"]


# Step 2: Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Step 3: Create the model
model = LinearRegression()


# Step 4: Train the model
model.fit(X_train, y_train)


# Step 5: Make predictions
predictions = model.predict(X_test)


# Step 6: Display results
print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(predictions)


# Step 7: Evaluate the model
mae = mean_absolute_error(
    y_test,
    predictions
)

print("\nMean Absolute Error:")
print(mae)