# load libraries
import numpy as np

# Create feature matrix
x = np.array([[1.1, 11.1],
              [2.2, 22.2],
              [3.3, 33.3],
              [4.4, 44.4],
              [np.nan, 55]])
# remove observations with missing values
x[~np.isnan(x).any(axis=1)]
