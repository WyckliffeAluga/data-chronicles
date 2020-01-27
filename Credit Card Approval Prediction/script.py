# import modules

import pandas as pd


## load dataset
applications = pd.read_csv('datasets/cc_approvals.data', header=None)

# print inspect that data ]
print(applications.head(5))
