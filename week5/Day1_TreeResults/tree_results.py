# Week 5 - Monday
# Assignment 4: Decision Tree Results Visualization

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

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

# Train Decision Tree
model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X, y)

# Feature importance
importance = model.feature_importances_

print("Study Hours Importance:", importance[0])
print("Attendance Importance:", importance[1])

# Bar chart
features = ["Study Hours", "Attendance"]

plt.bar(features, importance)

plt.title("Decision Tree Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.show()