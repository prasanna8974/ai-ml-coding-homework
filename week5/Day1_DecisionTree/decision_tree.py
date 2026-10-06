# Week 5 - Monday
# Assignment 2: Decision Tree Classifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features: Study Hours, Attendance
X = [
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 65],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90]
]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

# Create model
model = DecisionTreeClassifier(
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(
    y_test,
    prediction
)

print("Actual:", y_test)
print("Predicted:", prediction)
print("Accuracy:", accuracy)