
import matplotlib.image as img
import pandas as pd
import seaborn as sns
from scipy.cluster.vq import whiten , kmeans, vq
import matplotlib.pyplot as plt

image = img.imread("sea.jpeg")

r = []
g = []
b = []

for row in image :
    for pixel in row :

        temp_r , temp_g , temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

pixels = pd.DataFrame({"red": r,
                       "blue": b,
                       "green": g})

pixels['scaled_red'] = whiten(pixels.red)
pixels['scaled_blue'] = whiten(pixels.blue)
pixels['scaled_green'] = whiten(pixels.green)

# plot an elbow plot
distortions = []
num_clusters =  range(1,11)

for i in num_clusters :
    cluster_centers, distortion = kmeans(pixels[["scaled_red", "scaled_blue" , "scaled_green"]], i)
    distortions.append(distortion)

elbow_plot = pd.DataFrame({"num_clusters":num_clusters,
                           "distortions" :distortions})

sns.lineplot(x="num_clusters", y="distortions" , data=elbow_plot)

plt.xticks(num_clusters)
plt.show()

cluster_centers, _ = kmeans(pixels[["scaled_red", "scaled_blue", "scaled_green"]] , 2)

colors = []

# find stds
r_std , g_std, b_std = pixels[["red", "blue","green"]].std()

# scale back

for cluster_center in cluster_centers :
    scaled_r , scaled_g , scaled_b = cluster_center

    colors.append((
        scaled_r * r_std/255,
        scaled_g * g_std/255,
        scaled_b * b_std/255
    ))

plt.imshow([colors])
plt.show()
