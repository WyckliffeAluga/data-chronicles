"""
Rescaling the feature values of each observation so that they have a unit norm.

"""

# load libraries
from sklearn.preprocessing import Normalizer
import numpy as np

# Create feature matrix
X = np.array([[0.5, 0.5],
              [1.1, 3.4],
              [1.5, 20.2],
              [1.63, 34.4],
              [10.9, 3.3]])

# create a normalizer
normalizer = Normalizer(norm='l2')

# transform feature matrix
normalizer.transform(X)
