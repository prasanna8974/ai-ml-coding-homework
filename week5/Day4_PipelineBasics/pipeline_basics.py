# Week 5 - Thursday
# Assignment 3: Pipeline Basics
#
# Question:
# Create a pipeline using StandardScaler
# and LogisticRegression.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=500))
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Predict
predictions = pipeline.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)

print("Pipeline Accuracy:", accuracy)