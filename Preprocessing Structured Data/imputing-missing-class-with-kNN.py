# load libraries
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Create feature matrix with categorical feature
x = np.array([[0, 2.10, 1.45],
              [1, 1.18, 1.33],
              [0, 1.22, 1.27],
              [1, -0.21, -1.19]])

# Create feature matrix with missing values in the categorical feature
X_with_nan = np.array([[np.nan, 0.87, 1.31],
                       [np.nan, -0.67, -0.22]])

# train KNN learner
clf = KNeighborsClassifier(3, weights='distance')
trained_model = clf.fit(x[:,1:], x[:,0])

# predict missing values class
imputed_values = trained_model.predict(X_with_nan[:,1:])

# join column of predicted class with their other features
x_with_imputed = np.hstack((imputed_values.reshape(-1,1), X_with_nan[:,1:]))

# join the two feature matrices
np.vstack((x_with_imputed, x))
