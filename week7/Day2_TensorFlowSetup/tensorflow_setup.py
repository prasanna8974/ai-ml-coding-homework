import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

print("TensorFlow Version:", tf.__version__)

model = Sequential([
    Input(shape=(4,)),
    Dense(8, activation="relu"),
    Dense(3, activation="softmax")
])

model.summary()