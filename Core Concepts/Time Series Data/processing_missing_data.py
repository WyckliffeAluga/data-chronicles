import matplotlib.pyplot as plt

# return a boolean that notes where mssing valuesa re
missing = df.isna()

# interpolate linearly within missing windows
df_interp = df.interpolate("linear")

# plot the interpolated data in red and the data with missing values in black
ax = df_interp.plot(x="r")
df.plot(c="k", ax=ax , lw=2)


# use rolling method
def percent_change(values):
    """ Calculates the percentage change between the last value and the mean of
    previous values """

    # separate the last value and all previous values into variables
    previous_values = values[:-1]
    last_value = values[-1]

    # calculates the % difference between the last value and the mean of earlier values
    percentage_change = (last_value - np.mean(previous_values)) \
    / np.mean(previous_values)

    return percent_change

# plot the raw data
fig, axis = plt.subplot(1,2, figsize(10,5))
ax = df.plot(ax=axis[0])

# calculate % change and plot
ax = df.rolling(windows=20).aggregate(percent_change).plot(ax=axis[1])
ax.legend_.set_visible(False)


# detecting outliers
fig , axs = plt.subplots(1,2, figsize=(10,5))

for data, ax in zip([df, df_perc_change], axs):
    # calculate the maen / standard deviation for the data
    this_mean = data.mean()
    this_std  = data.std()

    # plot the data, with a window that is 3 standard deviations around the mean
    data.plot(ax=ax)
    ax.axhline(this_mean + this_std * 3, ls="--", c="r")
    ax.axhline(this_mean - this_std * 3, ls="--", c="r")

# replacing outliers using the thresholds

# center the data so the mean is 0

df_outlier_centered = df_outlier_perc - df_outlier_perc.mean()

# calculate standard deviation
std = df_outlier_perc.std()

# use the absolute value of each datapoint
# to make it easier to find outliers
outliers = np.abs(df_outlier_centered) > (std * 3)

# replace outliers with the median value
df_outlier_fixed = df_outlier_centered.copy()
df_outlier_fixed[outliers]  = np.nanmedian(df_outlier_fixed)

fig , axs = plt.subplots(1,2, figsize=(10,5))
df_outlier_centered.plot(ax=axs[0])
df_outlier_fixed.plot(ax=axs[1])
