
"""
The task is to predict whether a patient suffers from a liver disease using 10 features including Albumin, age and gender.
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score

df = pd.read_csv('datasets/indian_liver_patient_preprocessed.csv')
# split data
X = df.loc[:, df.columns != 'Liver_disease'].values
Y = df['Liver_disease'].values

X_train, X_test, y_train, y_test = train_test_split(X,Y,
                                                            test_size = 0.3,
                                                            random_state = 123)


# Instantiate dt
dt = DecisionTreeClassifier(max_depth=2, random_state=1)

# Instantiate ada
ada = AdaBoostClassifier(base_estimator=dt, n_estimators=180, random_state=1)

# Fit ada to the training set
ada.fit(X_train, y_train)

# Compute the probabilities of obtaining the positive class
y_pred_proba = ada.predict_proba(X_test)[:,1]

# Evaluate test-set roc_auc_score
ada_roc_auc = roc_auc_score(y_test , y_pred_proba)

# Print roc_auc_score
print('ROC AUC score: {:.2f}'.format(ada_roc_auc))
