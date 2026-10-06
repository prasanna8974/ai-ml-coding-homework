# Week 5 - Monday
# Assignment 3: Tree Depth Experiment

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features
X = [
    [1, 50], [2, 55], [3, 60], [4, 65],
    [5, 70], [6, 75], [7, 80], [8, 85],
    [9, 90], [10, 95], [3, 75], [7, 60]
]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

# Test different tree depths
for depth in [1, 2, 3, 4]:

    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    print(
        "Depth:", depth,
        "Accuracy:", accuracy
    )