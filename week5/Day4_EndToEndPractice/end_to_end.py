# Week 5 - Thursday
# Assignment 4: End-to-End ML Practice
#
# Question:
# Build a complete ML workflow to predict
# whether a student will pass or fail.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [40, 45, 50, 55, 60, 70, 75, 80, 90, 95],
    "Pass": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Step 2: Features and target
X = df[["Study_Hours", "Attendance"]]
y = df["Pass"]

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3,
    random_state=42, stratify=y
)

# Step 4: Create pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

# Step 5: Train model
model.fit(X_train, y_train)

# Step 6: Make predictions
predictions = model.predict(X_test)

# Step 7: Evaluate
accuracy = accuracy_score(y_test, predictions)

print("\nActual Values:", y_test.to_list())
print("Predictions:", predictions)
print("Model Accuracy:", accuracy)

# Step 8: Predict for a new student
new_student = pd.DataFrame({
    "Study_Hours": [7],
    "Attendance": [85]
})

result = model.predict(new_student)

print("\nNew Student Prediction:",
      "Pass" if result[0] == 1 else "Fail")