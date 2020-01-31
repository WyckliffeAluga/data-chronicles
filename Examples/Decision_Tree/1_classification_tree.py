
import data_prep

# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

SEED = 1

# Instantiate a DecisionTreeClassifier 'dt' with a maximum depth of 6
dt = DecisionTreeClassifier(max_depth=6, random_state=SEED)

# Instantiate data_prep

data = data_prep.Data()

name = ['auto',
        'breast_cancer',
        'liver_unprocessed',
        'liver_preprocessed',
        'bikes']

data = data.prep(name[0])

X_train = data['x_train']
X_test  = data['x_test']
y_train = data['y_train']
y_test  = data['y_test']

# Fit dt to the training set
dt.fit(X_train, y_train)

# Predict test set labels
y_pred = dt.predict(X_test)
print(y_pred[0:5])

# Predict test set labels
y_pred = dt.predict(X_test)

# Compute test set accuracy
acc = accuracy_score(y_pred, y_test)
print("Test set accuracy: {:.2f}".format(acc))
