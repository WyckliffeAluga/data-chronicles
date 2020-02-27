"""
one hot encoding allows us to turn nominal categorical data into features
with numerical values, while not mathematically imply any ordinal relationship
between the classes.
"""

# load libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Create NumPy array
x = np.array([['Texas'],
              ['California'],
              ['Texas'],
              ['Delaware'],
              ['Texas']])

# method one
# Create LabelBinzarizer object
one_hot = OneHotEncoder()

# One-hot encode data
one_hot.fit_transform(x)

# view classes
one_hot.categories_

# dumy feature
pd.get_dummies(x[:,0])
