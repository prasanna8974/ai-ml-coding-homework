# Week 5 - Friday
# Assignment 1: Student Performance Prediction
#
# Question:
# Build two ML models to predict student results.
# Compare their accuracy and find the best model.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Step 1: Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 4, 6, 8, 3, 5, 7, 9, 1, 10],
    "Attendance": [40, 50, 55, 60, 65, 70, 75, 80, 90, 95,
                   45, 58, 72, 85, 52, 68, 78, 92, 35, 98],
    "Pass": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
             0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Step 2: Features and target
X = df[["Study_Hours", "Attendance"]]
y = df["Pass"]

# Step 3: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3,
    random_state=42, stratify=y
)

# Step 4: Create models
models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression()
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=50, random_state=42
    )
}

# Step 5: Train and compare
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    results[name] = accuracy

    print(name, "Accuracy:", accuracy)

# Step 6: Find best model
best_model = max(results, key=results.get)

print("\nBest Model:", best_model)
print("Best Accuracy:", results[best_model])