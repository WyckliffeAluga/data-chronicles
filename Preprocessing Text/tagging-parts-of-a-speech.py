
# load libraries
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from nltk import word_tokenize

# create text
text_data = "Chris loved outdoor running"

# usre pre-trained part of speech tagger
text_tagged = pos_tag(word_tokenize(text_data))

# show
text_tagged
