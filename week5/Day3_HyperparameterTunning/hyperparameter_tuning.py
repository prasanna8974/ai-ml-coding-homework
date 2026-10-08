# Week 5 - Wednesday
# Assignment 2: Hyperparameter Tuning
#
# Question:
# Find the best Decision Tree parameters
# using GridSearchCV.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Load dataset
X, y = load_iris(return_X_y=True)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Parameters to test
parameters = {
    "max_depth": [1, 2, 3, 4, 5],
    "criterion": ["gini", "entropy"]
}

# Grid Search
grid = GridSearchCV(
    model,
    parameters,
    cv=5
)

# Train
grid.fit(X, y)

# Results
print("Best Parameters:", grid.best_params_)
print("Best Accuracy:", grid.best_score_)