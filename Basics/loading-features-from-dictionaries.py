
from sklearn.feature_extraction import DictVectorizer

# create a dictionary

soccer = [
         {'name': 'Vigil Van Dyke', 'position':'defender','age': 33.},
         {'name': 'Mane', 'position':'attack','age': 12.},
         {'name': 'Tret Anold', 'position':'winger','age': 18.}]

# convert dictionary to feature matrix
# create an object for the dictionary

vec = DictVectorizer()

# fit the transfrom
model = vec.fit_transform(soccer).toarray()

# get feature names
names = vec.get_feature_names()

print(names)
