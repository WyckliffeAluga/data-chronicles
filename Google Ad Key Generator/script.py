

## In this project I will create a prototype set of keywords for search campaoin for Sofas
# I will generate keywords for the following products:
#           Sofas
#           convertible sofas
#           love seats
#           recliners
#           Sofa beds

# the client offers a low-cost retailer offering many promotions and discounts.
# I will try to focus on these keywords
# I will aslo need to move away from luxury keywords asn topics
# Focus on tightly targerted keywords and make sure they are set to exact and phrase match

# import modules
from pprint import pprint
import pandas as pd

# STEP 1: Come up with a list of words that users might use to express their desire in buying low cost sofas

# List of words to pair with products
words = ['buy', 'price','discount', 'promotion','promo','shop']

# print list of words
#print(words)

# STEP 2: Combine the words with product names
products = ['sofas','convertible sofas', 'love seats','recliners','sofa beds']

# create an empty list
keywords_list = []

# loop through products
for product in products:
    # loop through words
    for word in words:
        # append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
# inspect keyword list
#pprint(keywords_list)

# create a DataFrame from list
keyword_df = pd.DataFrame.from_records(keywords_list)

# print the keywords DataFrame to explore it
#print(keyword_df.head(5))

# rename the columns
keyword_df.columns = ['Ad Group', 'keyword']

# add a campaign column
keyword_df['Campaign']  = 'SEM_Sofas'

# create a match type column
# add a criterion type column
keyword_df['Criterion Type'] = 'Exact'

# Duplicate all the keywords into phrase match
# make a copy of the keywords datafram
keywords_phrase = keyword_df.copy()

# change the criterion type match to phrase
keywords_phrase['Criterion Type'] = 'Phrase'

# append the DataFrames
keywords_final = keyword_df.append(keywords_phrase)

# print head
#print(keywords_final.tail())

# view the summary of the campaign worl
summary = keywords_final.groupby(['Ad Group','Criterion Type'])['keyword'].count()
#print(summary)

# save a csv file
keywords_final.to_csv('keywords.csv', index=False)
