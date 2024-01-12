# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-9fnuolKBgBLmw166PFwxJmIp5_q_luz

**BUILDING A CNN ARCHITECTURE FOR MNIST DATASET**


MNIST DATASET CONTAINS HANDWRITTEN IMAGES OF DIGITS
Code is run without using opencv
"""

from keras.datasets import mnist
import matplotlib.pyplot as plt

from keras.layers import Dense
from keras import layers

from keras.utils import to_categorical
from keras import Sequential

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_labels.shape)

plt.imshow(train_images[0])

train_images = train_images.reshape((60000, 28, 28,1)).astype('float32')/255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32')/255

print(train_images.shape)
print(test_images.shape)

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

print(train_labels.shape)
print(test_labels.shape)

model = Sequential()
model.add(layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (28, 28,1)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation = 'relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128, (3,3), activation = 'relu'))
model.add(layers.Flatten())
model.add(Dense(64, activation = 'relu'))
model.add(Dense(10, activation = 'sigmoid'))
model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['acc'])

model.fit(train_images, train_labels, batch_size = 20, validation_data = (test_images, test_labels), verbose = 1, epochs = 5)

train_acc = model.evaluate(train_images, train_labels, verbose = 1)
train_acc[1]*100

test_acc = model.evaluate(test_images, test_labels, verbose = 1)
test_acc[1]

print('Training acc: {}'.format(train_acc[1]*100))
print('Test acc: {}'.format(test_acc[1]*100))
