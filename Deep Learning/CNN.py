import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

# Set that the color channel value will be first
K.set_image_data_format('channels_first')

# Set seed
np.random.seed(0)

# Set image information
channels = 1
height = 28
width = 28

# Load data and target from MNIST data
(train_data, train_target), (test_data, test_target) = mnist.load_data()

# Reshape training image data into features
train_data = train_data.reshape(train_data.shape[0], channels, height, width)

# Reshape test image data into features
test_data = test_data.reshape(test_data.shape[0], channels, height, width)

# Rescale pixel intensity to between 0 and 1
train_features = train_data / 255
test_features = test_data / 255

# One-hot encode target
train_target = np_utils.to_categorical(train_target)
test_target = np_utils.to_categorical(test_target)
number_of_classes = test_target.shape[1]

# Set image information
channels = 1
height = 28
width = 28

# Load data and target from MNIST data
(train_data, train_target), (test_data, test_target) = mnist.load_data()

# Reshape training image data into features
train_data = train_data.reshape(train_data.shape[0], channels, height, width)

# Reshape test image data into features
test_data = test_data.reshape(test_data.shape[0], channels, height, width)

# Rescale pixel intensity to between 0 and 1
train_features = train_data / 255
test_features = test_data / 255

# One-hot encode target
train_target = np_utils.to_categorical(train_target)
test_target = np_utils.to_categorical(test_target)
number_of_classes = test_target.shape[1]

# Start neural network
network = Sequential()

# Add convolutional layer with 64 filters, a 5x5 window, and ReLU activation function
network.add(Conv2D(filters=64, kernel_size=(5, 5), input_shape=(channels, width, height), activation='relu'))

# Add max pooling layer with a 2x2 window
network.add(MaxPooling2D(pool_size=(2, 2)))

# Add dropout layer
network.add(Dropout(0.5))

# Add layer to flatten input
network.add(Flatten())

# # Add fully connected layer of 128 units with a ReLU activation function
network.add(Dense(128, activation='relu'))

# Add dropout layer
network.add(Dropout(0.5))

# Add fully connected layer with a softmax activation function
network.add(Dense(number_of_classes, activation='softmax'))
