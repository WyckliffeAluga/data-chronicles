

# function that processes data to be used for Decision tree examples
import pandas as pd
import glob
from sklearn.model_selection import train_test_split

files = glob.glob('datasets/*.csv')

names = []
for file in files:
    num = file
    num = num.split('\\')[1]
    num = num.split('.')
    names.append(num[0])

filenames = dict(zip(names,files ))
SEED = 1
frame = False
Name = 'auto'
test_size = 1

def splitter(x,y, size=test_size, random=SEED):
        # call function splitter to get the split data
        x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                            test_size = size,
                                                            random_state = random)
            # create a dictionary for the train
        split_values = {'x_train':x_train ,
                        'x_test':x_test ,
                        'y_train':y_train ,
                        'y_test':y_test}
        return split_values

class Data(object):
    """docstring for Data."""

    def __init__(self):
        super(Data, self).__init__()

    def split(self, name, size=0.2, seed=42, dataframe=False):
        global SEED
        SEED = seed
        global frame
        frame = dataframe
        global test_size
        test_size = size

        method_name='df_name_' + name
        method=getattr(self, method_name, lambda :'Invalid dataset please check the name and try again')
        return method()

    def df_name_auto(self):
        # read the automobile csc=v
        df = pd.read_csv(filenames['auto'])
        # get dummies to remove the object type
        df = pd.get_dummies(df, drop_first=True)
        # split the dataframe into features and labels then convert them into numpy arrays
        X = df.loc[:, df.columns != 'mpg'].values
        Y = df['mpg'].values

        out = splitter(X,Y,size=test_size, random=SEED)

        if frame == False:
            return out
        else :
            out['df'] = df
            return out

    def df_name_breast_cancer(self):
        df = pd.read_csv(filenames['wbc'])
        df = pd.get_dummies(df, drop_first=True)
        df = df.dropna(axis=1,how='all')

        X = df.loc[:, df.columns != 'diagnosis_M'].values
        Y = df['diagnosis_M'].values

        out = splitter(X,Y,size=test_size, random=SEED)

        if frame == False:
            return out
        else :
            out['df'] = df
            return out

    def df_name_liver_unprocessed(self):
        df = pd.read_csv(filenames['indian_liver_patient'])
        df = pd.get_dummies(df, drop_first=True)
        df = df.fillna('ffill')
        # split data
        
        X = df.loc[:, df.columns != 'Dataset'].values
        Y = df['Dataset'].values

        out = splitter(X,Y,size=test_size, random=SEED)

        if frame == False:
            return out
        else :
            out['df'] = df
            return out

    def df_name_liver_preprocessed(self):
        df = pd.read_csv(filenames['indian_liver_patient_preprocessed'])
        # split data
        X = df.loc[:, df.columns != 'Liver_disease'].values
        Y = df['Liver_disease'].values

        out = splitter(X,Y,size=test_size, random=SEED)

        if frame == False:
            return out
        else :
            out['df'] = df
            return out

    def df_name_bikes(self):
        df = pd.read_csv(filenames['bikes'])

        X = df.loc[:, df.columns != 'cnt'].values
        Y = df['cnt'].values

        out = splitter(X,Y,size=test_size, random=SEED)

        if frame == False:
            return out
        else :
            out['df'] = df
            return out
