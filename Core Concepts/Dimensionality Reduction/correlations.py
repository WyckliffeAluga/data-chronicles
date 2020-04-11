
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# create a correlation matrix
corr = df.corr()
# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))
# Add the mask to the heatmap
sns.heatmap(corr, mask=mask, cmap=cmap, center=0, linewidths=1, annot=True, fmt=".2f")
plt.show()


# removing highly correlatated features

# create positive correlation matrix
corr_df = df.corr().abs()

# create and apply mask
mask  = np.triu(np.ones_line(corr_df, dtype=bool))

tri_df = corr_df.mask(mask)

# find columns that meet threshold
to_drop = [c for c in tri_df.columns if any(tri_df[c] > 0.95)]

# drop the columns
reduced_df = df.drop(to_drop, axis=1)
