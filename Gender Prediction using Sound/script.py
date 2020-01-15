
# Analyze the gender distribution of children's book writers and use sound to match names to gender

import fuzzy
import pandas as pd
import numpy as np

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

# loop through first names and create the fuzzy equivalent

nysiis_name = []

for name in author_df['first_name'] :
    nytkids_yearly.append(fuzzy.nysiis(name))

# addd nysiis name on the author dataframe
author_df['nysiis_name'] = nysiis_name

# read the babies data base
babies_df = pd.read_csv('datasets/babynames_nysiis.csv' , sep=';')

# loop through babies_df to and fill up gender
gender = []

for index, row in babies_df.iterrows() :

    if row['perc_female']  >  row['perc_male'] :
        gender.append['F']

    elif row['perc_female'] < row['perc_male'] :
        gender.append['M']

    elif row['perc_female'] == row['perc_male'] :
        gender.append['N']

# write a function that returns the location of an element in a list
# where an item doesn't exist , it returns -1

def locate_in_list(a_list, element) :
    loc_of_name = a_list.index(element) if element in a_list else -1
    return loc_of_name

# loop through author_df and append the gender of each author
author_gender = []

for name in author_df['nysiis_name'] :
    author_idx = locate_in_list(list(babies_df['babynysiis']), name)

    if author_idx == -1 :
        author_gender.append('Unknown')

    else:
        author_gender.append(babies_df.iloc[author_idx, 3])

# adding authort_gender to the author df
author_df['author_gender'] = author_gender

# count the author's genders 
author_df['author_gender'].value_counts()
