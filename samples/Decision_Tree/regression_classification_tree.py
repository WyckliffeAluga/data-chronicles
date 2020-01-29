

# import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.linear_model import LinearRegression

# load data
df = pd.read_csv('auto.csv')

# print sample
#print(df.head(5))

# get dummies
df = pd.get_dummies(df)

# extract
features_colums = ['displ',
                    'hp',
                    'weight',
                    'accel',
                    'size',
                    'origin_Asia',
                    'origin_Europe',
                    'origin_US']
labels_column = ['mpg']

X = df[features_colums]
y = df[labels_column]
# split the data
x_train , x_test , y_train , y_test = train_test_split(X,
                                                      y,
                                                      test_size=0.2,
                                                      random_state=42)
# Instantiate dt
dt = DecisionTreeRegressor(max_depth=8,
             min_samples_leaf=0.13,
            random_state=3)

# Fit dt to the training set
dt.fit(x_train, y_train)


# Compute y_pred
y_pred = dt.predict(x_test)

# Compute mse_dt
mse_dt = MSE(y_pred, y_test)

# Compute rmse_dt
rmse_dt = np.sqrt(mse_dt)

# Instantiate linear model
le = LinearRegression()

# fit linear model
lr = le.fit(x_train, y_train)

# Predict test set labels
y_pred_lr = lr.predict(x_test)

# Compute mse_lr
mse_lr = MSE(y_pred_lr, y_test)

# Compute rmse_lr
rmse_lr = np.sqrt(mse_lr)

# Print rmse_lr
print('Linear Regression test set RMSE: {:.2f}'.format(rmse_lr))

# Print rmse_dt
print('Regression Tree test set RMSE: {:.2f}'.format(rmse_dt))
