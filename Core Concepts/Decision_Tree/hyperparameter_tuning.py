import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

# load the data
df = pd.read_csv('datasets/indian_liver_patient_preprocessed.csv')

# split data
X = df.loc[:, df.columns != 'Liver_disease'].values
y = df['Liver_disease'].values

SEED = 42
X_train, X_test, y_train , y_test = train_test_split(
                                                    X, y ,
                                                    test_size=0.3,
                                                    random_state=SEED
)
# Instantiate dt
dt = DecisionTreeClassifier(min_samples_leaf=0.13, random_state=SEED)
# Define params_dt
params_dt = {'max_depth': [2,3,4] ,
            'min_samples_leaf':[0.12,0.14,0.16,0.18]
}

# Instantiate grid_dt
grid_dt = GridSearchCV(estimator=dt,
                       param_grid=params_dt,
                       scoring='roc_auc',
                       cv=5,
                       n_jobs=-1)

grid_dt.fit(X_train, y_train)


# Extract the best estimator
best_model = grid_dt.best_estimator_

# Predict the test set probabilities of the positive class
y_pred_proba = best_model.predict_proba(X_test)[:,1]

# Compute test_roc_auc
test_roc_auc = roc_auc_score(y_test, y_pred_proba)

# Print test_roc_auc
print('Test set ROC AUC score: {:.3f}'.format(test_roc_auc))
