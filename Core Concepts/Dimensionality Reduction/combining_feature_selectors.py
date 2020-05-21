
from sklearn.linear_model import LassoCV
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

import numpy as np

# LassoCV
lcv = LassoCV()
lcv.fit(X_train, y_train)
lcv.score(X_test, y_test)

lcv_mask = lcv.coef_ != 0

sum(lcv_mask)

# rfe model with random forest
rfe_rf = RFE(restimator=RandomForestRegressor(), nfn_features_to_select=66 , step=5, verbose=1)

rfe_rf.fit(X_train, y_train)

rf_mask = rfe_rf.support_

# feature selection with gradient boosting
rfe_gb = RFE(esestimator=GradientBoostingRegressor(), nn_features_to_select=66 , step=5, verbose=1)

rfe_gb.fit(X_train, y_train)

gb_mask = rfe_gb.support_

votes = np.sum([lcv_mask, rf_mask, gb_mask], axis=0)

print(votes)

mask = votes >= 2

reduced_X = X.loc[:, mask]
