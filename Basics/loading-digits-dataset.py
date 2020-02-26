
# load libraries
from sklearn import datasets
import matplotlib.pyplot as plt

# load digits data
digits = datasets.load_digits()

# create feature matrix
x = digits.data

# create target matrix
y = digits.target

# view first observation as a matrix
first = digits.images[0]

# visualize the first obeservation feature as an image
plt.gray()
plt.matshow(first)
plt.show()
