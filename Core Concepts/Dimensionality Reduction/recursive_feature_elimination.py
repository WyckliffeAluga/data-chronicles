
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

rfe = RFE(estimator=LogisticRegression(), n_features_to_select=2, verbose=1)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)
X_train_std = scaler.fit_transform(X_train)

rfe.fit(X_train_std, y_train)

X_test_std = scaler.fit_transform(X_test)

# droping features
X.columns[rfe.support_]

print(dict(zip(X.columns, rfe.ranking_)))

print(accuracy_score(y_test, rfe.predict(X_test_std)))
