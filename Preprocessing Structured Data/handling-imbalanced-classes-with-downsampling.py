
# the strategy is to randomly sample without replacememtn from the minority class to create a new subset of observation equal in size ato the minority class

# load libraries
import numpy as np
from sklearn import datasets

# load iris data
iris = datasets.load_iris()

# extract x and y
x = iris.data
y = iris.target

# make iris data imbalance
# remove the first 40 observations
x = x[40:,:]
y = y[40:]

# create a binary target vector indicating if class 0
y = np.where((y==0), 0,1)


# downsample majority clkass to match minority class

# indices of each class' observation
idx_class_0 = np.where(y == 0)[0]
idx_class_1 = np.where(y == 1)[0]

# number of observations in each class
n_class_0 = len(idx_class_0)
n_class_1 = len(idx_class_1)
