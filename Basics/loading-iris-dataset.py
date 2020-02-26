
# load libraries
from sklearn import datasets
import matplotlib.pyplot as plt

# load iris dataset
iris = datasets.load_iris()

# create a feature matrix
x = iris.data

# create target vector
y = iris.target

print(x[0])
