# load libraries
from sklearn import preprocessing
import numpy as np

# Create feature
x = np.array([[-500.5],
              [-100.1],
              [0],
              [100.1],
              [900.9]])

# Create scaler
scaler = preprocessing.StandardScaler()

# Transform the feature
standardized = scaler.fit_transform(x)
