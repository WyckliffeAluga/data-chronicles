

# function that processes data to be used for Decision tree examples
import pandas as pd
from sklearn.model_selection import train_test_split

SEED = 1
frame = False
test_size = 1

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
        df = pd.read_csv('datasets/auto.csv')
        df = pd.get_dummies(df, drop_first=True)

        X = df.loc[:, df.columns != 'mpg'].values
        Y = df['mpg'].values

        x_train, x_test, y_train, y_test = train_test_split(
                                                            X, Y,
                                                            test_size = test_size,
                                                            random_state = SEED
        )

        out = {'x_train':x_train ,
               'x_test':x_test ,
               'y_train':y_train ,
               'y_test':y_test}
        if frame == False:
            return out
        else :
            out['df'] = df
            return out 
        
    def df_name_breast_cancer(self):
        df = pd.read_csv('datasets/wbc.csv')
        df = pd.get_dummies(df, drop_first=True)
        df = df.dropna(axis=1,how='all')
        return df

    def df_name_liver_unprocessed(self):
        df = pd.read_csv('datasets/indian_liver_patient.csv')
        df = pd.get_dummies(df, drop_first=True)
        df = df.fillna('ffill')
        return df

    def df_name_liver_preprocessed(self):
        df = pd.read_csv('datasets/indian_liver_patient_preprocessed.csv')
        return df
