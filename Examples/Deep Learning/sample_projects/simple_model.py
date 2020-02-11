

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
import pandas as pd

# load the dataset
df = pd.read_csv('datasets/hourly_wages.csv')

#predictors_columns = ['union', 'education_years', 'experience_yrs', 'age', 'female', 'marr', 'south', 'manufacturing', 'construction']
predictors = df.loc[:, df.columns != 'wage_per_hour'].values
target     = df['wage_per_hour'].values
print(predictors)
# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]

# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))

# Add the second layer
model.add(Dense(32, activation='relu'))

# Add the output layer
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Verify that model contains information from compiling
print("Loss function: " + model.loss)

# Fit the model
model.fit(predictors, target)
