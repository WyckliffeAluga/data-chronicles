# laod libraries
import pandas as pd
from pytz import all_timezones

# Create datetime
pd.Timestamp('2017-05-01 06:00:00', tz='Europe/London')

# Create datetime
date = pd.Timestamp('2017-05-01 06:00:00')

# Set time zone
date_in_london = date.tz_localize('Europe/London')

# Change time zone
date_in_london.tz_convert('Africa/Abidjan')
