import pandas as pd
import matplotlib.pyplot as plt

# creating a time-shifted dataframe

# data is a pandas Series containing time series data
data = pd.Series(...)

# shifts
shifts = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7]

# create a dictionary of time-shifted ata
many_shifts  = {"lag_{}".format(ii) : data.shift(ii) for ii in shifts}

# convert them into a dataframe
many_shifts = pd.DataFrame(many_shifts)

# Fit a model usign these input featues
model = Ridg()
model.fit(many_shifts, data)

# visualize the fit model coefficients
fig , ax = plt.subplots()
ax.bar(many_shifts.columns, model.coef_)
ax.set(xlabel="Coefficient name", ylabel="Coefficient value")

# set formattign so it looks nice
plt.setp(ax.get_xticklabel(), rotation=45, horizontalalighment="right")



# These are the "time lags"
shifts = np.arange(1, 11).astype(int)

# Use a dictionary comprehension to create name: value pairs, one pair per shift
shifted_data = {"lag_{}_day".format(day_shift): df_perc.shift(day_shift) for day_shift in shifts}

# Convert into a DataFrame for subsequent use
df_perc_shifted = pd.DataFrame(shifted_data)

# Plot the first 100 samples of each
ax = df_perc_shifted.iloc[:100].plot(cmap=plt.cm.viridis)
df_perc.iloc[:100].plot(color='r', lw=2)
ax.legend(loc='best')
plt.show()

# Replace missing values with the median for each column
X = prices_perc_shifted.fillna(np.nanmedian(prices_perc_shifted))
y = prices_perc.fillna(np.nanmedian(prices_perc))

# Fit the model
model = Ridge()
model.fit(X, y)


def visualize_coefficients(coefs, names, ax):
    # Make a bar plot for the coefficients, including their names on the x-axis
    ax.bar(names, coefs)
    ax.set(xlabel='Coefficient name', ylabel='Coefficient value')

    # Set formatting so it looks nice
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    return ax

# Visualize the output data up to "2011-01"
fig, axs = plt.subplots(2, 1, figsize=(10, 5))
y.loc[:'2011-01'].plot(ax=axs[0])

# Run the function to visualize model's coefficients
visualize_coefficients(model.coef_, prices_perc_shifted.columns, ax=axs[1])
plt.show()


# auto regression with a smoother time series
# Visualize the output data up to "2011-01"
fig, axs = plt.subplots(2, 1, figsize=(10, 5))
y.loc[:'2011-01'].plot(ax=axs[0])

# Run the function to visualize model's coefficients
visualize_coefficients(model.coef_, prices_perc_shifted.columns, ax=axs[1])
plt.show()
