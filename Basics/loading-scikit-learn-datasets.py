
# load libraries
from sklearn import datasets
import matplotlib.pyplot as plt

# load digits dataset
boston = datasets.load_boston()

# create a feature matrix
x = boston.data

# create a target vector
y = boston.target

# display features value for the first observation as floats
features = ['{:f}'.format(x) for x in x[0]]

print(features)
