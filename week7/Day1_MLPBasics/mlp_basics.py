# Week 7 - Monday
# Assignment 2: MLP Basics

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2,
    random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build MLP model
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    max_iter=1000,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Number of Features:", X.shape[1])
print("Hidden Layers:", model.hidden_layer_sizes)
print("Accuracy:", accuracy_score(y_test, predictions))
print("First 10 Predictions:", predictions[:10])