
# Analyze the gender distribution of children's book writers and use sound to match names to gender

import fuzzy
import pandas as pd

# explore the output
fuzzy.nysiis('John')

# testing equivalence of similar sounding words
fuzzy.nysiis('Jane')

# read the files
author_df = pd.read_csv('datasets/nytkids_yearly.csv', sep=';')

# loop through authors names to extract the authors first names

first_name = []
for name in author_df['Author'] :
    first_name.append(name.split()[0])

# add first name as a column
author_df['first_name'] = first_name

# sample the head
#print(author_df.head())
