# Define params_dt
params_dt = {'max_depth': [2,3,4] , 
            'min_samples_leaf':[0.12,0.14,0.16,0.18]
}

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

# Instantiate grid_dt
grid_dt = GridSearchCV(estimator=dt,
                       param_grid=params_dt,
                       scoring='roc_auc',
                       cv=5,
                       n_jobs=-1)
                       
                       
