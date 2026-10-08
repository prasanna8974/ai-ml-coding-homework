# Week 5 - Wednesday
# Assignment 4: Accuracy Comparison

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_iris(return_X_y=True)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=500)
}

results = []

# Train and evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    accuracy = accuracy_score(y_test, prediction)

    results.append([name, accuracy])

# Comparison table
df = pd.DataFrame(
    results,
    columns=["Model", "Accuracy"]
)

print("\nMODEL ACCURACY COMPARISON:")
print(df.to_string(index=False))

# Best model
best = df.loc[df["Accuracy"].idxmax()]
print("\nBest Model:", best["Model"])
print("Best Accuracy:", best["Accuracy"])