
# load libraries
import pandas as pd
from sklearn.datasets import make_regression

# generate features, outputs and true coefficients of 100 samples
features, output, coef = make_regression(n_samples=100,
                                        # three features
                                        n_features=3,
                                        # where only 2 are useful
                                        n_informative=2,
                                        # a single target value per observation
                                        n_targets=1,
                                        # 0.0 standard deviation of the gaussian noise
                                        noise=0.0,
                                        # show the true coefficient used to generate the datasets
                                        coef = True)

#create dataframes
features = pd.DataFrame(features, columns=['Liverpool', 'Manchester City', 'Chelsea'])
output = pd.DataFrame(output, columns=['Score coefficient'])
coef  = pd.DataFrame(coef, columns=['True Coeffient Values'])
print(coef.head())
