
"""
A perceptron learner was one of the earliest machine learning techniques and still from the foundation of many modern neural networks.

"""

# load libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# load iris dataset
iris = datasets.load_iris()

# create features and target
x = iris.data
y = iris.target

# split the data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

# train the scaler which standardizes all the features to have a mean of 0 and unit varianze
sc = StandardScaler()
sc.fit(x_train)

# apply the scaler to the x training and x_test data
x_train_std = sc.transform(x_train)
x_test_std  = sc.transform(x_test)

# train a perceptron learer
# create an object with 40 iterations nand learning rate of 0.1
ppn = Perceptron(verbose=0, max_iter=40, eta0=0.1, random_state=0)

# train the perceptron
ppn.fit(x_train_std, y_train)

# apply the trained ppn on the x data
y_pred = ppn.predict(x_test_std)

# print the accuraty
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
