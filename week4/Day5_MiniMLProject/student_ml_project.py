# Week 4 - Friday
# Mini Machine Learning Project
#
# Project:
# Student Pass/Fail Prediction
#
# Goal:
# Build a classification model that predicts whether
# a student will pass or fail based on study hours
# and attendance.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# --------------------------------
# Step 1: Create Dataset
# --------------------------------

data = {
    "Study_Hours": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 9,
        10, 11, 12
    ],

    "Attendance": [
        45, 50, 55, 58, 62,
        65, 68, 70, 74, 76,
        80, 82, 85, 88, 90,
        92, 95, 97
    ],

    "Pass": [
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1
    ]
}


students = pd.DataFrame(data)


print("STUDENT DATASET:")
print(students)


# --------------------------------
# Step 2: Inspect Dataset
# --------------------------------

print("\nFirst 5 Rows:")
print(students.head())


print("\nDataset Shape:")
print(students.shape)


print("\nMissing Values:")
print(students.isnull().sum())


# --------------------------------
# Step 3: Features and Target
# --------------------------------

X = students[
    ["Study_Hours", "Attendance"]
]


y = students["Pass"]


print("\nFeatures:")
print(X.head())


print("\nTarget:")
print(y.head())


# --------------------------------
# Step 4: Train-Test Split
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


print("\nTraining Records:")
print(len(X_train))


print("Testing Records:")
print(len(X_test))


# --------------------------------
# Step 5: Feature Scaling
# --------------------------------

scaler = StandardScaler()


X_train_scaled = scaler.fit_transform(
    X_train
)


X_test_scaled = scaler.transform(
    X_test
)


# --------------------------------
# Step 6: Create Model
# --------------------------------

model = LogisticRegression()


# --------------------------------
# Step 7: Train Model
# --------------------------------

model.fit(
    X_train_scaled,
    y_train
)


# --------------------------------
# Step 8: Make Predictions
# --------------------------------

predictions = model.predict(
    X_test_scaled
)


print("\nActual Results:")
print(y_test.values)


print("\nPredicted Results:")
print(predictions)


# --------------------------------
# Step 9: Accuracy
# --------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)


print("\nModel Accuracy:")
print(accuracy)


print("\nAccuracy Percentage:")
print(accuracy * 100, "%")


# --------------------------------
# Step 10: Confusion Matrix
# --------------------------------

cm = confusion_matrix(
    y_test,
    predictions
)


print("\nConfusion Matrix:")
print(cm)


# --------------------------------
# Step 11: Classification Report
# --------------------------------

report = classification_report(
    y_test,
    predictions,
    zero_division=0
)


print("\nClassification Report:")
print(report)


# --------------------------------
# Step 12: Predict New Student
# --------------------------------

new_student = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [78]
})


new_student_scaled = scaler.transform(
    new_student
)


new_prediction = model.predict(
    new_student_scaled
)


print("\nNEW STUDENT PREDICTION:")


if new_prediction[0] == 1:

    print("Prediction: PASS")

else:

    print("Prediction: FAIL")