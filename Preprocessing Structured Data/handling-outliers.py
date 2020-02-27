
# load library
import pandas as pd
import numpy as np

# create dataframe
houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032]
houses['Bathrooms'] = [2, 3.5, 2, 116]
houses['Square_Feet'] = [1500, 2500, 1500, 48000]


""" To handle outliers we can :
1. Drop : not a great option we lose a lot of information
2. Mark : safest option.see if the outliers have any effect
3. Rescale: log values so outliers don't have as great an effect.
"""

# drop the observations greater than 20
houses[houses['Bathrooms'] < 20]

# mark
# create feature based on boolean condition
houses['Outlier'] = np.where(houses['Bathrooms'] < 20, 0 , 1)

# Rescale
# log feature
houses['Log_of_square_feet'] = [np.log(x) for x in houses['Square_Feet']]

houses
