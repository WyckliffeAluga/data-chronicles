import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functools import partial

# Define a rolling window with Pandas, excluding the right-most datapoint of the window
df_perc_rolling = df_perc.rolling(20, min_periods=5, closed='right')

# Define the features you'll calculate for each window
features_to_calculate = [np.min, np.max, np.mean, np.std]

# Calculate these features for your rolling window object
features = df_perc_rolling.aggregate(features_to_calculate)

# Plot the results
ax = features.loc[:"2011-01"].plot()
prices_perc.loc[:"2011-01"].plot(ax=ax, color='k', alpha=.2, lw=3)
ax.legend(loc=(1.01, .6))
plt.show()

# percentiles and partials
percentiles = [1, 10, 25, 50, 75, 90, 99]

# Use a list comprehension to create a partial function for each quantile
percentile_functions = [partial(np.percentile, q=percentile) for percentile in percentiles]

# Calculate each of these quantiles on the data using a rolling window
df_perc_rolling = df_perc.rolling(20, min_periods=5, closed='right')
features_percentiles = df_perc_rolling.aggregate(percentile_functions)

# Plot a subset of the result
ax = features_percentiles.loc[:"2011-01"].plot(cmap=plt.cm.viridis)
ax.legend(percentiles, loc=(1.01, .5))
plt.show()

# Extract date features from the data, add them as columns
df_perc['day_of_week'] = df_perc.index.dayofweek
df_perc['week_of_year'] =df_perc.index.weekofyear
df_perc['month_of_year'] =df_perc.index.month

# Print prices_perc
print(df_perc)
