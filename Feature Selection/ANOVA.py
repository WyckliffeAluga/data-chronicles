"""
If the features are categorical, calculate a chi-square (χ2) statistic between each feature and the target vector.
However, if the features are quantitative, compute the ANOVA F-value between each feature and the target vector.

The F-value scores examine if, when we group the numerical feature by the target vector, the means for each group are significantly different
"""

# load libraries
from sklearn import datasets
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# load iris data
iris = datasets.load_iris()

# create features and target
x = iris.data
y = iris.target

# create a SelectKBest object to selevt features with two best ANOVA F-values
fvalue_selector = SelectKBest(f_classif, k=2)

# appply the SelectKBest object to the features and target
x_kbest = fvalue_selector.fit_transform(x,y)

# Show results
print('Original number of features:', x.shape[1])
print('Reduced number of features:', x_kbest.shape[1])
