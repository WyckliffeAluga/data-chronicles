import plot_classifier as pcl
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datasets/indian_liver_patient_preprocessed.csv')

X = df.loc[:, df.columns != 'Liver_disease'].values
y = df['Liver_disease'].values

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                    test_size=0.3,
                                    random_state=42)

# Set the regularization strength
model = LogisticRegression(C=0.1)

# Fit and plot
model.fit(X_train,y_train)
#pcl.plot_classifier(X_train,y_train, model,proba=True)

# Predict probabilities on training points
prob = model.predict_proba(X)
print("Maximum predicted probability", np.max(prob))

lr = LogisticRegression()
lr.fit(X_train,y_train)

# Get predicted probabilities
proba = lr.predict_proba(X_train)

# Sort the example indices by their maximum probability
proba_inds = np.argsort(np.max(proba,axis=1))

# Show the most confident (least ambiguous) digit
show_digit(proba_inds[-1], lr)

# Show the least confident (most ambiguous) digit
show_digit(proba_inds[0], lr)
