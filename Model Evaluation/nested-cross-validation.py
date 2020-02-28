# Load required packages
from sklearn import datasets
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.svm import SVC

# Load the data
dataset = datasets.load_breast_cancer()

# Create X from the features
X = dataset.data

# Create y from the target
y = dataset.target

# Create a scaler object
sc = StandardScaler()

# Fit the scaler to the feature data and transform
X_std = sc.fit_transform(X)

# Create a list of 10 candidate values for the C parameter
C_candidates = dict(C=np.logspace(-4, 4, 10))

# Create a gridsearch object with the support vector classifier and the C value candidates
clf = GridSearchCV(estimator=SVC(), param_grid=C_candidates)

# Fit the cross validated grid search on the data
clf.fit(X_std, y)

# Show the best value for C
clf.best_estimator_.C

cross_val_score(clf, X_std, y)
