from sklearn.feature_selection import VarianceThreshold

# Create a VarianceThreshold feature selector
sel = VarianceThreshold(threshold=0.001)

# Fit the selector to normalized df
sel.fit(df / df.mean())

# Create a boolean mask
mask = sel.get_support()

# Apply the mask to create a reduced dataframe
reduced_df = df.loc[:, mask]

print("Dimensionality reduced from {} to {}.".format(df.shape[1], reduced_df.shape[1]))
