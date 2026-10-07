# Week 5 - Tuesday
# Assignment 1: Random Forest Basics

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features: Study Hours, Attendance
X = [
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 65],
    [5, 70],
    [6, 75],
    [7, 80],
    [8, 85],
    [9, 90],
    [10, 95]
]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# Create Random Forest
model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    prediction
)

print("Actual:", y_test)
print("Predicted:", prediction)
print("Accuracy:", accuracy)