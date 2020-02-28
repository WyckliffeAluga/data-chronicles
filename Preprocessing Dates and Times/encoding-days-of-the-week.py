
# load libray
import pandas as pd

# Create dates
dates = pd.Series(pd.date_range('2/2/2002', periods=3, freq='M'))

# show days of the week
dates.dt.weekday_name
