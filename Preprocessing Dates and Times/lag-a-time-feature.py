# load library
import pandas as pd

# create data frames
df = pd.DataFrame()

# Create data
df['dates'] = pd.date_range('1/1/2001', periods=5, freq='D')
df['stock_price'] = [1.1,2.2,3.3,4.4,5.5]

# Lagged values by one row
df['previous_days_stock_price'] = df['stock_price'].shift(1)
