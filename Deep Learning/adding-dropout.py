"""
Trains an ensemble of subnetworks with shared parameters.
ensemble contains all subnetworks possible, constrained by hyperparameters controlling the
pobability of a particular mask.
"""

# Load libraries
import numpy as np
from keras.datasets import imdb
from keras.preprocessing.text import Tokenizer
from keras import models
from keras import layers

# Set random seed
np.random.seed(0)

# Set the number of features we want
number_of_features = 1000

# Load data and target vector from movie review data
(train_data, train_target), (test_data, test_target) = imdb.load_data(num_words=number_of_features)

# Convert movie review data to a one-hot encoded feature matrix
tokenizer = Tokenizer(num_words=number_of_features)
train_features = tokenizer.sequences_to_matrix(train_data, mode='binary')
test_features = tokenizer.sequences_to_matrix(test_data, mode='binary')

# start neural network
net = models.Sequential()

# add a droupour layer for input layer
net.add(layers.Dropout(0.2, input_shape=(number_of_features,)))

# add fully connected layer with a ReLu activation function
net.add(layers.Dense(units=19, activation='relu'))

# add a Dropout layer for previous hidden layer
net.add(layers.Dropout(0.5))

# Add fully connected layer with a ReLU activation function
net.add(layers.Dense(units=16, activation='relu'))

# Add a dropout layer for previous hidden layer
net.add(layers.Dropout(0.5))

# Add fully connected layer with a sigmoid activation function
net.add(layers.Dense(units=1, activation='sigmoid'))

# Compile neural network
net.compile(loss='binary_crossentropy', # Cross-entropy
                optimizer='rmsprop', # Root Mean Square Propagation
                metrics=['accuracy']) # Accuracy performance metric

# Train neural network
history = net.fit(train_features, # Features
                      train_target, # Target vector
                      epochs=3, # Number of epochs
                      verbose=0, # No output
                      batch_size=100, # Number of observations per batch
                      validation_data=(test_features, test_target)) # Data for evaluation
