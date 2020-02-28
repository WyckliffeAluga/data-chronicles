
"""
Stemming reduces a word to its stem.
The result is less readble by humans but makes the text more comparable across observations.

It identifies and remove affixes while keeping the root meaning of the word.
"""

# load library
from nltk.stem.porter import PorterStemmer

# create word tokens
tokenized_words = ['i', 'am', 'humbled', 'by', 'this', 'traditional', 'meeting']

# create stemmer
porter = PorterStemmer()

# apply stemmer
[porter.stem(word) for word in tokenized_words]
