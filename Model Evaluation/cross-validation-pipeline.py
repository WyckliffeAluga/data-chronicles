from sklearn.datasets import load_iris
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from sklearn import svm

# Load the iris test data
iris = load_iris()

# View the iris data features for the first three rows
iris.data[0:3]

# View the iris data target for first three rows. '0' means it flower is of the setosa species.
iris.target[0:3]

# Create a pipeline that scales the data then trains a support vector classifier
classifier_pipeline = make_pipeline(preprocessing.StandardScaler(), svm.SVC(C=1))

# KFold/StratifiedKFold cross validation with 3 folds (the default)
# applying the classifier pipeline to the feature and target data
scores = cross_val_score(classifier_pipeline, iris.data, iris.target, cv=3)

scores.mean()
