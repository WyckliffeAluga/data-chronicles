
import pandas as pd

# Create data frame
df = pd.DataFrame()

# Create two datetime features
df['Arrived'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-04-2017')]
df['Left'] = [pd.Timestamp('01-01-2017'), pd.Timestamp('01-06-2017')]

# Calculate duration between features
df['Left'] - df['Arrived']

# Calculate duration between features
pd.Series(delta.days for delta in (df['Left'] - df['Arrived']))
