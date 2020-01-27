# import modules

import pandas as pd


## load dataset
applications = pd.read_csv('datasets/cc_approvals.data', header=None)

# print inspect that data ]
#print(applications.head(5))

"""

As you can see from our first glance at the data, the dataset has a mixture of numerical
 and non-numerical features. This can be fixed with some preprocessing """
 
