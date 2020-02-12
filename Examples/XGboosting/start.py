
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

 df = pd.read_csv('datasets/indian_liver_patient_preprocessed.csv')

X = df.loc[:, df.columns != 'SalePrice'].values
y = df['SalePrice'].values

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size=0.3,
                                    random_state=42)
