
# laod libraries
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle
from sklearn.externals import joblib

# load data
iris = datasets.load_iris()

# create x and y
x , y = iris.data , iris.target

# train model
clf = LogisticRegression(verbose=0, random_state=0)
clf.fit(x,y)

# Save the model as a pickle in a file
joblib.dump(clf, 'filename.pkl')

# Load the model from the file
clf_from_joblib = joblib.load('filename.pkl')

# Use the loaded model to make predictions
clf_from_joblib.predict(X)
