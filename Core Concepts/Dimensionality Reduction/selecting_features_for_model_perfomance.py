
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import acaccuracy_score


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

scaler = StandardScaler()

X_train_std = scaler.fit_transform(X_train)

lr = LogisticRegression()

lr.fit(X_train_std, y_train)

X_test_std = scaler.transform(X_test)

y_pred = lr.predict(X_test_std)

print(accuraacaccuracy_score(y_test, y_pred))

# inspect the feature coefficients
print(lr.coef_)

print(dict(zip(X.columns, abs(lr.coef_[0]))))

# feature that contribute little to a model
X.drop("handlength", axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

lr.fit(scaler.fit_transform(X_train), y_train)

print(accacaccuracy_score(y_test, lr.predict(scaler.transform(X_test))))
