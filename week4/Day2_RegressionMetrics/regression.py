# Week 4 - Tuesday
# Assignment 3: MAE and MSE
#
# Question:
# Train a Linear Regression model.
# Make predictions.
# Calculate MAE and MSE.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


# Create dataset
data = {
    "Advertising_Cost": [
        100, 200, 300, 400, 500,
        600, 700, 800, 900, 1000
    ],

    "Sales": [
        20, 28, 35, 43, 52,
        58, 67, 74, 85, 91
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# Feature
X = df[["Advertising_Cost"]]

# Target
y = df["Sales"]


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


# Display results
print("\nActual Sales:")
print(y_test.values)

print("\nPredicted Sales:")
print(predictions)


# Calculate MAE
mae = mean_absolute_error(
    y_test,
    predictions
)


# Calculate MSE
mse = mean_squared_error(
    y_test,
    predictions
)


print("\nMean Absolute Error (MAE):")
print(mae)

print("\nMean Squared Error (MSE):")
print(mse)