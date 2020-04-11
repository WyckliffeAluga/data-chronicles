# import modules

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

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

#print(applications.info())

# drop drivers licence and zipcode

# drop features 11 and 13
applications = applications.drop(columns=[11,13], axis=1)

# change the dataframe into an array
applications = applications.values

# separate features from lables
X, y = applications[:,0:13] , applications[:,13]


# split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
                                X, y,
                                test_size=0.33,
                                random_state=42
)

# instantiate MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
rescladedX_train = scaler.fit_transform(X_train)
rescaledX_test  = scaler.fit_transform(X_test)

# Instantiate a LogisticRegression classifier with default parameter values
logreg = LogisticRegression()

# Fit logreg to the train set
logreg.fit(rescladedX_train, y_train)

# Use logreg to predict instances from the test set and store it
y_pred = logreg.predict(rescaledX_test)

# Get the accuracy score of logreg model and print it
print("Accuracy of logistic regression classifier: ", y_pred)

# Print the confusion matrix of the logreg model
print(confusion_matrix(y_test, y_pred))


"""
For the confusion matrix, the first element of the of the
first row of the confusion matrix denotes the true negatives
meaning the number of negative instances (denied applications)
predicted by the model correctly. And the last element of the second row
 of the confusion matrix denotes the true positives meaning the number of
 positive instances (approved applications) predicted by the model correctly. """

 # Define the grid of values for tol and max_iter
tol = [0.01, 0.001, 0.0001]
max_iter = [100, 150, 200]

# Create a dictionary where tol and max_iter are keys and the lists of their values are corresponding values
param_grid = dict({'tol':tol, 'max_iter':max_iter})

# Instantiate GridSearchCV with the required parameters
grid_model = GridSearchCV(estimator=logreg, param_grid=param_grid, cv=5)

# Use scaler to rescale X and assign it to rescaledX
rescaledX = scaler.fit_transform(X)

# Fit data to grid_model
grid_model_result = grid_model.fit(rescaledX, y)

# Summarize results
best_score = grid_model_result.best_score_
best_params= grid_model_result.best_params_
print("Best: %f using %s" % (best_score, best_params))
