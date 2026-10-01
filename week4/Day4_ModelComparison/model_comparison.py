# Week 4 - Thursday
# Assignment 3: Model Comparison
#
# Question:
# Train Logistic Regression and KNN models.
# Compare their accuracy scores.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Create dataset
data = {
    "Study_Hours": [
        1, 2, 2, 3, 3,
        4, 5, 6, 7, 8,
        9, 10, 11, 12
    ],

    "Attendance": [
        50, 55, 60, 62, 65,
        70, 75, 80, 85, 88,
        92, 95, 96, 98
    ],

    "Pass": [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        1, 1, 1, 1
    ]
}


# Create DataFrame
students = pd.DataFrame(data)

print("Student Dataset:")
print(students)


# Features
X = students[
    ["Study_Hours", "Attendance"]
]


# Target
y = students["Pass"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)


# -----------------------------
# Feature Scaling
# -----------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


# -----------------------------
# Logistic Regression
# -----------------------------

logistic_model = LogisticRegression()

logistic_model.fit(
    X_train_scaled,
    y_train
)

logistic_predictions = logistic_model.predict(
    X_test_scaled
)

logistic_accuracy = accuracy_score(
    y_test,
    logistic_predictions
)


# -----------------------------
# KNN
# -----------------------------

knn_model = KNeighborsClassifier(
    n_neighbors=3
)

knn_model.fit(
    X_train_scaled,
    y_train
)

knn_predictions = knn_model.predict(
    X_test_scaled
)

knn_accuracy = accuracy_score(
    y_test,
    knn_predictions
)


# -----------------------------
# Results
# -----------------------------

print("\nActual Results:")
print(y_test.values)

print("\nLogistic Regression Predictions:")
print(logistic_predictions)

print("\nKNN Predictions:")
print(knn_predictions)


print("\nLogistic Regression Accuracy:")
print(logistic_accuracy)


print("\nKNN Accuracy:")
print(knn_accuracy)


# Compare models
print("\nMODEL COMPARISON:")

if logistic_accuracy > knn_accuracy:

    print(
        "Logistic Regression has higher accuracy "
        "on this test split."
    )

elif knn_accuracy > logistic_accuracy:

    print(
        "KNN has higher accuracy "
        "on this test split."
    )

else:

    print(
        "Both models have the same accuracy "
        "on this test split."
    )