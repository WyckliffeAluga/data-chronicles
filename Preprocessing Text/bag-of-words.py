"""
converts text to a matrix where every row is an observation and every
feature is a unique word. The value of each element in the matrix is
either a binary indicator marking the presence of that word or an intergert
of the number of times that workd appears.
"""

# Load library
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Create text
text_data = np.array(['I love Brazil. Brazil!',
                      'Sweden is best',
                      'Germany beats both'])

# Create the bag of words feature matrix
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

# Show feature matrix
bag_of_words.toarray()

# Get feature names
feature_names = count.get_feature_names()

# Create data frame
pd.DataFrame(bag_of_words.toarray(), columns=feature_names)
