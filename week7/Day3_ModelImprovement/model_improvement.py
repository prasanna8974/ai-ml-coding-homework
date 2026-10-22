import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

# Compare two models
experiments = [(64, 2), (128, 5)]

for neurons, epochs in experiments:

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(28, 28)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(neurons, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    model.fit(X_train, y_train, epochs=epochs, verbose=0)

    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

    print(f"Neurons: {neurons}")
    print(f"Epochs: {epochs}")
    print(f"Test Accuracy: {accuracy:.4f}")
    print("--------------------")