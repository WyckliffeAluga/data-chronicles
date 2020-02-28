
"""
TF-IDF is a measure of originality of a word by comparing the
number of times a word appears in a doc with the nnumber docs the
word appears in.
"""

# load libraries
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# create text
# Create text
text_data = np.array(['I love Brazil. Brazil!',
                      'Sweden is best',
                      'Germany beats both'])

# Create the tf-idf feature matrix
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)

# Show tf-idf feature matrix
feature_matrix.toarray()

# show tf-idf feature matrix
tfidf.get_feature_names()

# create data frame
pd.DataFrame(feature_matrix.toarray(), columns=tfidf.get_feature_names())
