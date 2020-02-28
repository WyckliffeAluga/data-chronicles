# import libraries
import pandas as pd
import numpy as np

# Create date
time_index = pd.date_range('01/01/2010', periods=5, freq='M')

# Create data frame, set index
df = pd.DataFrame(index=time_index)

# Create feature with a gap of missing values
df['Sales'] = [1.0,2.0,np.nan,np.nan,5.0]

# Interpolate missing values
df.interpolate()

# forward-fill
df.ffill()

# back-fill
df.bfill()

# interpolate missing values
df.interpolate(limit=1, limit_direction='forward')
