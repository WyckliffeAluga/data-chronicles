
# load libraries
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split

# load data
iris = load_iris()

# create features and target
x , y = iris.data , iris.target

# split data into training and test set
x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=0)

# create a dumy classifier
dummy = DummyClassifier(strategy='uniform', random_state=1)

# train model
dummy.fit(x_train, y_train)

# get accuracy score
dummy.score(x_test, y_test)
