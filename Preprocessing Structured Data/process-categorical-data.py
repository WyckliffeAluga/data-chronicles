# load libraries
from sklearn import preprocessing
import pandas as pd

# createa data frame
raw_data = {'patient': [1, 1, 1, 2, 2],
           'obs': [1, 2, 3, 1, 2],
           'treatment': [0, 1, 0, 1, 0],
           'score': ['strong', 'weak', 'normal', 'weak', 'strong']}
df = pd.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score'])

# fit the label encoder
# create a label (categoriey) encorder object
le = preprocessing.LabelEncoder()

# fit  the encoder to the pandas column
le.fit(df['score'])

# apply the categories to the pandas column
le.transform(df['score'])

# Convert some integers into their category names
print(le.inverse_transform([2, 2, 1]))
