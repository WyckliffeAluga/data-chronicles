

# function that processes data to be used for Decision tree examples
import pandas as pd

class Data(object):
    """docstring for Data."""

    def __init__(self):
        super(Data, self).__init__()

    def dataset(self, name):
              method_name='df_name_' + name
              method=getattr(self, method_name, lambda :'Invalid dataset please check the name and try again')
              return method()

    def df_name_auto(self):
            df = pd.read_csv('auto.csv')
            df = pd.get_dummies(df, drop_first=True)
            return def
            
    def df_name_breast_cancer(self):
             return 'one'
    def df_name_liver_processed(self):
            return 'two'
    def df_name_liver_unprocessed(self):
            return 'three'
