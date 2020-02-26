
# load libraries
import pandas as pd

# create a features
# Create features
df = pd.DataFrame({'Score': ['Low',
                             'Low',
                             'Medium',
                             'Medium',
                             'High']})

# Create mapper
scale_mapper = {'Low':1,
                'Medium':2,
                'High':3}

# Map feature values to scale
df['Scale'] = df['Score'].replace(scale_mapper)

df
