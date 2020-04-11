
from scipy.cluster.vq import kmeans, vq
import matplotlib.pyplot as plt
import seaborn as sns

cluster_centers, _ = kmeans(df[["scaled_x" , "scaled_y"]], 3)

df["cluster_labels"] , _ = vq(df[["scaled_x" , "scaled_y"]] , cluster_centers)

sns.scatterplot(x="scaled_x" , y="scaled_y" , hue="cluster_labels" , data=df)
plt.show()


# how many clusters???
# creating an elbow plot

distortions = []

num_clusters = range(2,7)

for i in num_clusters:
    centroids, distortion = kmeans(df[["scaled_x" , "scaled_y"]], i)
    distortions.append(distortion)

elbow_plot_data = pd.DataFrame({'num_clusters': num_clusters,
                                'distortions': distortions})

sns.lineplot(x="num_clusters" , y="distortions" , data=elbow_plot_data)

plt.show()


# uniform clustering patterns

# Generate cluster centers
cluster_centers, distortion = kmeans(mouse[["x_scaled" , "y_scaled"]], 3)

# Assign cluster labels
mouse['cluster_labels'], distortion_list = vq(mouse[["x_scaled","y_scaled"]], cluster_centers)

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled',
                hue='cluster_labels', data = mouse)
plt.show()
