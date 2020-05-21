
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.vq import kmeans, vq
import re

data = "It is a lovely weather today. I hope this doesn't change in the coming weeks."
num_clusters = 3
def remove_noise (text, stop_words=[]) :
    tokens = word_tokenize(text)
    cleaned_tokens =  []

    for token in tokens:
        token = re.sub("[^A-Za-z0-9]+", "" , token)
        if len(token) > 1 and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


tfidf_vectorizer = TfidfVectorizer(max_df=0.8 , max_features=50 , min_df=0.2 , tokenizer=remove_noise)

tdidf_matrix = tfidf_vectorizer.fit_transform(data)

cluster_centers , distortion = kmeans(tdidf_matrix.todense() , num_clusters)

terms = tfidf_vectorizer.get_feature_names()

for i in range(num_clusters) :
    center_terms = dict(zip(terms, list(cluster_centers[i])))
    sorted_terms = sorted(center_terms, key=center_terms.get, reversed=True)
    print(sorted_terms[:3])
