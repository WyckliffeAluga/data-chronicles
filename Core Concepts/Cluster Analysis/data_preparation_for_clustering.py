

# Normalization of data
# rescale data to a std of 1

from scipy.cluster.vq import whiten
from matplotlib import pyplot as plt

data = [5,1,3,3,2,3,3,8,1,2,2,3,5]

scaled_data = whiten(data)
print(scaled_data)

plt.plot(data, label="original")
plt.plot(scaled_data, label="scaled")
plt.legend()
plt.show()

# scale small data
# Prepare data
rate_cuts = [0.0025, 0.001, -0.0005, -0.001, -0.0005, 0.0025, -0.001, -0.0015, -0.001, 0.0005]

# Use the whiten() function to standardize the data
scaled_data = whiten(rate_cuts)

# Plot original data
plt.plot(rate_cuts, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

plt.legend()
plt.show()
