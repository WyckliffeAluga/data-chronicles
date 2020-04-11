
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt

Z = linkage(df[["x_whiten","y_whiten"]],
            method="ward",
            metric="euclidean")

dn = dendrogram(Z)

plt.show()
