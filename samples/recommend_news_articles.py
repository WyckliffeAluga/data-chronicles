

# import modules
from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize
import pandas as pd

# instantiate NMF
nmf = NMF(n_components=6)

# fit transform to get nmf_features
nmf_features = nmf.fit_transform(articles)

# calculate cosine similarity
norm_features = normalize(nmf_features)

# current article
current_article = norm_features[23,:]

similarities = norm_features.dot(current_article) # cosine similarities

# create a dataf rame
df=pd.DataFrame(norm_features, index=titles)

# current article
current_article = df.loc['Dog bites man']

# similarities
similarities = df.dot(current_article)

print(similarities.nlargest())
