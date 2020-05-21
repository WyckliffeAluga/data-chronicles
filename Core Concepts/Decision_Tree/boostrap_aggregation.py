import pandas as pd
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Import BaggingClassifier
from sklearn.ensemble import BaggingClassifier

# Instantiate dt
dt = DecisionTreeClassifier(random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=1)

df = pd.read_csv('datasets/indian_liver_patient_preprocessed.csv')
# split data
X = df.loc[:, df.columns != 'Liver_disease'].values
Y = df['Liver_disease'].values

X_train, X_test, y_train, y_test = train_test_split(X,Y,
                                                            test_size = 0.3,
                                                            random_state = 42)
# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate acc_test
acc_test = accuracy_score(y_pred, y_test)
print('Test set accuracy of bc: {:.2f}'.format(acc_test))
