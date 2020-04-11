
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from scipy.optimize import minimize

df = pd.read_csv('datasets/indian_liver_patient_preprocessed.csv')

X = df.loc[:, df.columns != 'Liver_disease'].values
y = df['Liver_disease'].values

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size=0.3,
                                    random_state=42)

# Mathematical functions for logistic and hinge losses
def log_loss(raw_model_output):
   return np.log(1+np.exp(-raw_model_output))
def hinge_loss(raw_model_output):
   return np.maximum(0,1-raw_model_output)

# Create a grid of values and plot
grid = np.linspace(-2,2,1000)
plt.plot(grid, log_loss(grid), label='logistic')
plt.plot(grid, hinge_loss(grid), label='hinge')
plt.legend()
plt.show()


# The logistic loss, summed over training examples
def my_loss(w):
    s = 0
    for i in range(X_train.shape[0]):
        raw_model_output = w@X_train[i]
        s = s + log_loss(raw_model_output * y_train[i])
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X_train[0]).x
print(w_fit)

# Compare with scikit-learn's LogisticRegression
lr = LogisticRegression(fit_intercept=False, C=1000000).fit(X_train,y_train)
print(lr.coef_)
