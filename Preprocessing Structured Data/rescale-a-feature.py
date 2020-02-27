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
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

# Scale feature
x_scale = minmax_scale.fit_transform(x)
