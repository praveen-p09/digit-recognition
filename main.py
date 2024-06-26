import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist=tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train=tf.keras.utils.normalize(x_train, axis=1)
x_test=tf.keras.utils.normalize(x_test, axis=1)

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train,y_train,epochs=5)

model.save('handwritten_digit_model.keras')
# model = tf.keras.models.load_model('handwritten_digit_model.keras')

# Evaluating the model on test set
# loss, accuracy = model.evaluate(x_test, y_test)
# print("Loss:", loss)
# print("Accuracy:", accuracy)

# Predicting custom images
# image_number = 0
# while os.path.isfile(f"images/digit{image_number}.png"):
#     try:
#         img = cv2.imread(f"images/digit{image_number}.png", cv2.IMREAD_GRAYSCALE)
#         img = cv2.resize(img, (28, 28))  # Ensure the image is 28x28
#         img = np.invert(img)  # Invert the image if necessary
#         img = img / 255.0  # Normalize the image
#         img = img.reshape(1, 28, 28)  # Reshape to the model's input shape
#
#         prediction = model.predict(img)
#         print(f"The digit is {np.argmax(prediction)}")
#         plt.imshow(img[0], cmap=plt.cm.binary)
#         plt.show()
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         image_number += 1
