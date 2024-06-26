# -*- coding: utf-8 -*-
"""mnist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YyEldHMa_Cg9bTAhQeWPC4NvaiTJxTJX
"""

import tensorflow as tf
import numpy as np
from keras.datasets import mnist
from PIL import Image

(x_train,y_train),(x_test,y_test)=mnist.load_data()

x_test=x_test/255
x_train=x_train/255

model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10, batch_size=64, verbose=1)

loss,accuracy=model.evaluate(x_test,y_test)
print(f"Loss{loss}, accuracy:{accuracy}")

image_index=1
image=x_test[image_index]
label=y_test[image_index]

image=image.reshape(1,28,28)

prediction = np.argmax(model.predict(image),axis=-1)

print("The original index:",label)
print("The predicted index:", prediction)

