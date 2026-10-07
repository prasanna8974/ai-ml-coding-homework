# Week 5 - Tuesday
# Assignment 4: Feature Importance

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

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

# Create model
model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

# Train model
model.fit(X, y)

# Get feature importance
importance = model.feature_importances_

print("Study Hours Importance:", importance[0])
print("Attendance Importance:", importance[1])

# Create chart
features = ["Study Hours", "Attendance"]

plt.bar(features, importance)

plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.show()