# load libraries
import pandas as pd
from pytz import all_timezones

# Create ten dates
dates = pd.Series(pd.date_range('2/2/2002', periods=10, freq='M'))

# Set time zone
dates_with_abidjan_time_zone = dates.dt.tz_localize('Africa/Abidjan')

# View pandas series
dates_with_abidjan_time_zone
