# Week 4 - Thursday
# Assignment 1: KNN Classifier
#
# Question:
# Create a classification dataset.
# Train a K-Nearest Neighbors (KNN) classifier.
# Try different values of K and compare accuracy.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


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
    test_size=0.25,
    random_state=42
)


# Create KNN model with K = 3
model = KNeighborsClassifier(
    n_neighbors=3
)


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


# Calculate accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)


print("\nAccuracy with K = 3:")
print(accuracy)


# Try different K values
print("\nDifferent K Values:")

for k in [1, 3, 5]:

    knn = KNeighborsClassifier(
        n_neighbors=k
    )

    knn.fit(
        X_train,
        y_train
    )

    prediction = knn.predict(X_test)

    score = accuracy_score(
        y_test,
        prediction
    )

    print(
        "K =", k,
        "Accuracy =", score
    )