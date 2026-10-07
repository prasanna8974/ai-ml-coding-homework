# Week 5 - Tuesday
# Assignment 2: Decision Tree vs Random Forest

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features
X = [
    [1, 50], [2, 55], [3, 60], [4, 65],
    [5, 70], [6, 75], [7, 80], [8, 85],
    [9, 90], [10, 95]
]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42
)

# Decision Tree
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

tree_prediction = tree.predict(X_test)

tree_accuracy = accuracy_score(
    y_test,
    tree_prediction
)

# Random Forest
forest = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

forest.fit(X_train, y_train)

forest_prediction = forest.predict(X_test)

forest_accuracy = accuracy_score(
    y_test,
    forest_prediction
)

# Results
print("Decision Tree Accuracy:", tree_accuracy)
print("Random Forest Accuracy:", forest_accuracy)

if tree_accuracy > forest_accuracy:
    print("Decision Tree performed better.")

elif forest_accuracy > tree_accuracy:
    print("Random Forest performed better.")

else:
    print("Both models have the same accuracy.")