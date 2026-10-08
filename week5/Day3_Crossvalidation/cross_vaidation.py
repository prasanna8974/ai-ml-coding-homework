# Week 5 - Wednesday
# Assignment 1: Cross Validation Basics
#
# Question:
# Use cross_val_score to evaluate a Decision Tree.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

# Load dataset
X, y = load_iris(return_X_y=True)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Perform 5-fold cross validation
scores = cross_val_score(
    model, X, y, cv=5
)

print("Accuracy Scores:", scores)
print("Average Accuracy:", scores.mean())