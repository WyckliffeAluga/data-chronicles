from matplotlib import pyplot as plt


x = [80,93,86,98,86,9,15,3,10,20,44,56,49,62,44]
y = [87,96,95,92,92,57,49,47,59,55,25,2,10,24,10]

plt.scatter(x,y)
plt.show()


# basics of cluster analysis

# hierarchical clustering
from scipy.cluster.hierarchy import linkage, fcluster
import seaborn as sns
import pandas as pd


x = [80.1,93.1,86.6,98.5,86.4,9.5,15.2,3.4,10.4,20.3,44.2,56.8,49.2,62.5,44.0]
y = [87.2,96.1,95.6,92.4,57.7,49.4,47.3,59.1,55.5,25.6,2.1,10.9,24.1,10.3]

df = pd.DataFrame({"x_cord": x, "y_cord":y})

z = linkage(df, 'ward') # calculate distances between clusters
df["cluster_labels"] = fcluster(z, 3, criterion="maxclust")

sns.scatterplot(x="x_cord", y="y_cord", hue="cluster_labels", data=df)

plt.show()

# K means clustering
from scipy.cluster.vq import kmeans, vq
import random

random.seed((1000, 2000))

centroids,_ = kmeans(df,3)
df["cluster_labels"], _ = vq(df, centroids)

sns.scatterplot(x="x_cord", y="y_cord", hue="cluster_labels", data=df)

plt.show()
