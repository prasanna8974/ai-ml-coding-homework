import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28, 28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_train, y_train, epochs=3, verbose=0)

# Predict first test image
prediction = model.predict(X_test[:1], verbose=0)
predicted_digit = np.argmax(prediction[0])

print("Actual Digit:", y_test[0])
print("Predicted Digit:", predicted_digit)

plt.imshow(X_test[0], cmap="gray")
plt.title(f"Actual: {y_test[0]} | Predicted: {predicted_digit}")
plt.axis("off")
plt.show()