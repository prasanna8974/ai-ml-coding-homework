# Week 7 - Monday
# Assignment 3: MLP Experiments

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    random_state=42,
    stratify=iris.target
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

experiments = [
    ((5,), 100, "relu"),
    ((10,), 300, "relu"),
    ((20, 10), 500, "relu"),
    ((10,), 500, "tanh")
]

for layers, iterations, activation in experiments:

    model = MLPClassifier(
        hidden_layer_sizes=layers,
        max_iter=iterations,
        activation=activation,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\nHidden Layers:", layers)
    print("Max Iterations:", iterations)
    print("Activation:", activation)
    print("Actual Iterations:", model.n_iter_)
    print("Accuracy:", round(accuracy, 3))