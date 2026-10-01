# Week 4 - Thursday
# Assignment 4: Practice Dataset
#
# Question:
# Perform a complete classification workflow
# using the Iris dataset.
#
# Steps:
# 1. Load dataset
# 2. Identify features and target
# 3. Split data
# 4. Scale features
# 5. Train KNN model
# 6. Make predictions
# 7. Evaluate model

import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# --------------------------------
# Step 1: Load Iris dataset
# --------------------------------

iris = load_iris()


# Convert features into DataFrame
X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)


# Create target
y = pd.Series(
    iris.target,
    name="Flower_Type"
)


print("IRIS FEATURES:")
print(X.head())


print("\nTARGET:")
print(y.head())


print("\nFLOWER CLASSES:")
print(iris.target_names)


# --------------------------------
# Step 2: Train-Test Split
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining Records:")
print(len(X_train))

print("Testing Records:")
print(len(X_test))


# --------------------------------
# Step 3: Feature Scaling
# --------------------------------

scaler = StandardScaler()


# Learn scaling from training data
X_train_scaled = scaler.fit_transform(
    X_train
)


# Apply same scaling to test data
X_test_scaled = scaler.transform(
    X_test
)


# --------------------------------
# Step 4: Create KNN Model
# --------------------------------

model = KNeighborsClassifier(
    n_neighbors=3
)


# --------------------------------
# Step 5: Train Model
# --------------------------------

model.fit(
    X_train_scaled,
    y_train
)


# --------------------------------
# Step 6: Make Predictions
# --------------------------------

predictions = model.predict(
    X_test_scaled
)


print("\nActual Values:")
print(y_test.values)


print("\nPredicted Values:")
print(predictions)


# --------------------------------
# Step 7: Accuracy
# --------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)


print("\nAccuracy:")
print(accuracy)


# --------------------------------
# Step 8: Confusion Matrix
# --------------------------------

cm = confusion_matrix(
    y_test,
    predictions
)


print("\nConfusion Matrix:")
print(cm)


# --------------------------------
# Step 9: Classification Report
# --------------------------------

report = classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
)


print("\nClassification Report:")
print(report)