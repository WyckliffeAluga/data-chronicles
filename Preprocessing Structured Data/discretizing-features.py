# load libraries
from sklearn.preprocessing import Binarizer
import numpy as np

# Create feature
age = np.array([[6],
                [12],
                [20],
                [36],
                [65]])

# Create binarizer
binarizer = Binarizer(18)
# Transform feature
binarizer.fit_transform(age)

# Bin feature
np.digitize(age, bins=[20,30,64])
