
# load library
import pandas as pd

# Create datetimes
time_index = pd.date_range('01/01/2010', periods=5, freq='M')

# Create data frame, set index
df = pd.DataFrame(index=time_index)

# Create feature
df['Stock_Price'] = [1,2,3,4,5]

# calculate rolling mean
df.rolling(window=2).mean()

# identify max value in rolling time window
df.rolling(window=2).max()
