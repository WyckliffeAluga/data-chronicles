
# load libraries
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# make data x,y with 200 samples
x, y = make_blobs(n_samples=200,
                 # two feeatur variables
                  n_features=2,
                 #three clusters
                  centers=3,
                  # with .5 cluster standard deviation
                  cluster_std=0.5,
                  # then shuffle
                  shuffle=True)

# create a scatter plot of the first and second featurs
plt.scatter(x[:,0], x[:,1])
