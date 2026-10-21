from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target,
    test_size=0.2, random_state=42, stratify=iris.target
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential([
    Input(shape=(4,)),
    Dense(16, activation="relu"),
    Dense(3, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_train, y_train, epochs=50, verbose=0)

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("Test Loss:", round(loss, 4))
print("Test Accuracy:", round(accuracy, 4))

predictions = model.predict(X_test[:5], verbose=0)

print("Predicted Classes:", predictions.argmax(axis=1))
print("Actual Classes:", y_test[:5])