# Week 5 - Tuesday
# Assignment 3: Overfitting Check

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features
X = [
    [1, 50], [2, 55], [3, 60], [4, 65],
    [5, 70], [6, 75], [7, 80], [8, 85],
    [9, 90], [10, 95], [4, 80], [7, 65]
]

# Target
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

# Create and train model
model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
train_prediction = model.predict(X_train)
test_prediction = model.predict(X_test)

# Accuracy
train_accuracy = accuracy_score(
    y_train,
    train_prediction
)

test_accuracy = accuracy_score(
    y_test,
    test_prediction
)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

# Compare
if train_accuracy > test_accuracy:
    print("Model may be overfitting.")
else:
    print("No clear overfitting in this result.")