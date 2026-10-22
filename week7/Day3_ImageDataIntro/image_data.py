import tensorflow as tf
import matplotlib.pyplot as plt

# Load handwritten digit images
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("Training Images:", X_train.shape)
print("Testing Images:", X_test.shape)
print("First Image Label:", y_train[0])

# Display the first image
plt.imshow(X_train[0], cmap="gray")
plt.title(f"Digit: {y_train[0]}")
plt.axis("off")
plt.show()