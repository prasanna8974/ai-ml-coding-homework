# Week 5 - Wednesday
# Assignment 3: Best Parameters Analysis
#
# Question:
# Find and analyze the best Decision Tree parameters.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Load dataset
X, y = load_iris(return_X_y=True)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Parameters
params = {
    "max_depth": [1, 2, 3, 4, 5],
    "criterion": ["gini", "entropy"]
}

# Grid Search
grid = GridSearchCV(model, params, cv=5)
grid.fit(X, y)

# Best results
print("Best Parameters:", grid.best_params_)
print("Best Accuracy:", grid.best_score_)

# Analysis
print("\nMODEL ANALYSIS:")
print("Best Depth:", grid.best_params_["max_depth"])
print("Best Criterion:", grid.best_params_["criterion"])
print("GridSearchCV selected the highest average CV score.")