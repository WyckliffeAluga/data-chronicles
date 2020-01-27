# import modules

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

## load dataset
applications = pd.read_csv('datasets/cc_approvals.data', header=None)

# print inspect that data ]
#print(applications.head(5))

"""

As you can see from our first glance at the data, the dataset has a mixture of numerical
 and non-numerical features. This can be fixed with some preprocessing """

# let us look at some other properties

# print summary stats
#print(applications.describe())
#print('\n')

# print dataframe information
#print(applications.info())

# inspeact missing values
print(applications.tail(5))


# replace missing "?" with NaN
applications  = applications.replace('?', np.NaN)

# impute the missing values with mean imputation
applications.fillna(applications.mean(), inplace=True)

# count number of NaN
#print(applications.isnull().sum())

# iterate over each valuer
for col in applications :
    # check if column is of object type
    if applications[col].dtypes == 'object' :
        # impute witht he most frequent values
        applications = applications.fillna(applications[col].value_counts().index[0])

# couount the number ofn NaNs
print(applications.isnull().sum())

"""
Converting all the non-numeric values into numeric ones. This is done
 because not only it results in a faster computation
  but also many machine learning models (like XGBoost)
  (and especially the ones developed using scikit-learn) require the
   data to be in a strictly numeric format.
  """
 # instantiate LabelEncoder
le = LabelEncoder()

  # iterate over alll the values of each column
  for col in applications.columns:
      # compare if the dtype if object
      if applications[col].dtypes =='object':
          applications[col] = le.fit_transform(applications[col])
      # use LabelEncoder to do numeric transformation

print(applications.info())
