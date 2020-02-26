
# load libraries
from sklearn.datasets import make_classification
import pandas as pd

# create simulated data with 100 samples
features, output = make_classification(n_samples=100,
                                        # ten features
                                        n_features=10,
                                        # five features that actually predict the class of the output
                                        n_informative=5,
                                        # five features that are random and unrelated to the class of the output
                                        n_redundant =5,
                                        #three output classes
                                        n_classes=3,
                                        # with 20% of observations in the first class, 30% in the seond and 50 in the third
                                        # none makes balanced classes
                                        weights = [.2,.3,.5])

# view the data
data = pd.DataFrame(features)

# output
output = pd.DataFrame(output)
