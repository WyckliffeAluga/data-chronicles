# load libraries

import numpy as np
import pandas as pd

# Create feature matrix
x = np.array([[1, 2],
              [6, 3],
              [8, 4],
              [9, 5],
              [np.nan, 4]])

# remove observations with missing values
x[~np.isnan(x).any(axis=1)]

# remove using pandas
# create a dataframe

# laod data as a dataframe
df = pd.DataFrame(x, columns=['play','score'])

# remove the na
df.dropna()
