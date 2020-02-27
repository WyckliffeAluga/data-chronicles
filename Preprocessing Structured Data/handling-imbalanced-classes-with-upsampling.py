"""
In upsampling, for every observation in the majority class,
we randomly select an observation from the minority class with replacement.
The end result is the same number of observations from the minority and majority classes.
"""

# load libraries
import numpy as np
from sklearn import datasets

# load iris data
iris = datasets.load_iris()

# create a feature matrix
x = iris.data

# create a target vector
y = iris.target

# make iris dataset imbalanced
# remove first 40 observations

x = x[40:,:]
y = y[40:]

# create binary target vector indicating if class if 00

y = np.where((y==0), 0, 1)

# indices of each class observations
i_class0  = np.where(y ==0)[0]
i_class1  = np.where(y ==1)[0]

# number of observations in each class
n_class0 = len(i_class0)
n_class1 = len(i_class1)

# for every observation in class 1, randomly sample from class 0 with replacement
i_class0_upsampled = np.random.choice(i_class0, size=n_class1, replace=True)

# join together class 0's upsampled target vector  with class 1 target vector
np.concatenate((y[i_class0_upsampled], y[i_class1]))
