# Week 4 - Monday
# Assignment: Train-Test Split

import pandas as pd
from sklearn.model_selection import train_test_split

# Create dataset
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 96],
    "Marks": [50, 55, 60, 65, 70, 75, 80, 84, 90, 95]
}

students = pd.DataFrame(data)

print("Original Dataset:")
print(students)

# Features
X = students[["Study_Hours", "Attendance"]]

# Target
y = students["Marks"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nX Train:")
print(X_train)

print("\nX Test:")
print(X_test)

print("\ny Train:")
print(y_train)

print("\ny Test:")
print(y_test)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))