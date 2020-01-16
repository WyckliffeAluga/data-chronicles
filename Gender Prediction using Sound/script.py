
# Analyze the gender distribution of children's book writers and use sound to match names to gender

import fuzzy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    nysiis_name.append(fuzzy.nysiis(name))

# addd nysiis name on the author dataframe
author_df['nysiis_name'] = nysiis_name

# read the babies csv
babies_df = pd.read_csv('datasets/babynames_nysiis.csv' , sep=';')

# loop through babies_df to and fill up gender
gender = []

for index, row in babies_df.iterrows() :

    if row['perc_female']  >  row['perc_male'] :
        gender.append('F')

    elif row['perc_female'] < row['perc_male'] :
        gender.append('M')

    elif row['perc_female'] == row['perc_male'] :
        gender.append('N')

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
print(author_df['author_gender'].value_counts())

# create a list of unique years,
years = sorted(author_df['Year'].unique())

# initializing lists
males_by_yr    = []
females_by_yr  = []
unknowns_by_yr = []

# looping through years to find the number of male , female and unknowns by year

for year in years :

    males_by_yr.append(len(author_df[
                (author_df['author_gender'] == 'M') &
                (author_df['Year'] == year)
    ]))

    females_by_yr.append(len(author_df[
                (author_df['author_gender'] == 'F') &
                (author_df['Year'] == year)
    ]))
    unknowns_by_yr.append(len(author_df[
                (author_df['author_gender'] == 'Unknown') &
                (author_df['Year'] == year)
    ]))

# print the yearly valies
data = np.array([males_by_yr, females_by_yr, unknowns_by_yr])
headers = ['males', 'females', 'unkowns']
data = pd.DataFrame(data, headers, years)

# plot bar chart
_=plt.bar(yers, unknowns_by_yr, title='Foreign born authors')
plt.show()

# create a new list where 0.25 is aded to each other
years_shifted = [year + 0.25 for year in years]

# plot males
_=plt.bar(years, males_by_yr, width=0.25, color='lightblue')
# plot female
_=plt.plot(years_shifted, females_by_yr, width=0.25, color='red')
plt.show()
