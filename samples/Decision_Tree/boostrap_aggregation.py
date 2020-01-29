import pandas as pd
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Import BaggingClassifier
from sklearn.ensemble import BaggingClassifier

# Instantiate dt
dt = DecisionTreeClassifier(random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=1)

# load the data
df = pd.read_csv('indian_liver_patient.csv')

# get dummies
df = pd.get_dummies(df, drop_first=True)


# split data
X = df.loc[:, df.columns != 'Dataset'].values
y = df['Dataset'].values

SEED = 42
X_train, X_test, y_train , y_test = train_test_split(
                                                    X, y ,
                                                    test_size=0.2,
                                                    random_state=SEED)
# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate acc_test
acc_test = accuracy_score(y_pred, y_test)
print('Test set accuracy of bc: {:.2f}'.format(acc_test))
