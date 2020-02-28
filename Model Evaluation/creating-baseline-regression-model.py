# Load libraries
from sklearn.datasets import load_boston
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
boston = load_boston()

# Create features
X, y = boston.data, boston.target

# Make test and training split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Create a dummy regressor
dummy_mean = DummyRegressor(strategy='mean')

# "Train" dummy regressor
dummy_mean.fit(X_train, y_train)

# Create a dummy regressor that always predit a contant value
dummy_constant = DummyRegressor(strategy='constant', constant=20)

# "Train" dummy regressor
dummy_constant.fit(X_train, y_train)

# Get R-squared score
dummy_constant.score(X_test, y_test)  
