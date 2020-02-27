
# load libraries
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
import pandas as pd

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])

# create a dumy variables for every unique cateogry in df.city
pd.get_dummies(df['city'])

# conveert strings catergorical names to intergers
integer_data = preprocessing.LabelEncoder().fit_transform(df['city'])

# convert interger catergorical representations to onehot encodings
preprocessing.OneHotEncoder().fit_transform(integer_data.reshape(-1,1)).toarray()
