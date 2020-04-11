import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error as MSE

# Set SEED for reproducibility
SEED = 1

# load data
df = pd.read_csv('datasets/auto.csv')

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
SEED = 1
x_train , x_test , y_train , y_test = train_test_split(X,
                                                      y,
                                                      test_size=0.3,
                                                      random_state=SEED)

# Instantiate a DecisionTreeRegressor dt
dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.26, random_state=SEED)

# Compute the array containing the 10-folds CV MSEs
MSE_CV_scores = - cross_val_score(dt, x_train, y_train, cv=10,
                       scoring='neg_mean_squared_error',
                       n_jobs=-1)

# Compute the 10-folds CV RMSE
RMSE_CV = (MSE_CV_scores.mean())**(0.5)

# Print RMSE_CV
print('CV RMSE: {:.2f}'.format(RMSE_CV))

""" evaluate the training set RMSE
achieved by the regression tree """

# Fit dt to the training set
dt.fit(x_train, y_train)

# Predict the labels of the training set
y_pred_train = dt.predict(x_train)

# Evaluate the training set RMSE of dt
RMSE_train = (MSE(y_train, y_pred_train))**(0.5)

# Print RMSE_train
print('Train RMSE: {:.2f}'.format(RMSE_train))


"""
Notice how the training error is roughly equal to the 10-folds CV error .

this model is underfitting the
 training set as the model is too
 constrained to capture the nonlinear
 dependencies between features and labels."""
