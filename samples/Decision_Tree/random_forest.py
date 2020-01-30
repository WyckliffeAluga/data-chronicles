# use bike sharing demand data 
# x features 12 columns 
# Hr, 
# Holiday , 
# workingday 
# temp 
# hum 
# windspeed 
# instant 
# mnth 
# yr 
# clear to partly cloudy 
# light precipitation 
# misty 

# Import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

# Instantiate rf
rf = RandomForestRegressor(n_estimators=25,
            random_state=2)
            
# Fit rf to the training set    
rf.fit(X_train, y_train) 

# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Predict the test set labels
y_pred = rf.predict(X_test)

# Evaluate the test set RMSE
rmse_test = (MSE(y_test, y_pred))** (0.5)

# Print rmse_test
print('Test set RMSE of rf: {:.2f}'.format(rmse_test))
