
# hi
# in this project I will try to analyze tv data to answer questions like
# What are the most extreme outcomes in super bowl
# How does the game affect tv viewership
# how have viewership , TV ratings and ad cost evolved over time
# Who is the most prolific musician in terms of half time perfomances

# import modules

import pandas as pd
import matplotlib.pyplot as plt

# style the plots
plt.style.use('seaborn')

# Load all csv data
superBowls = pd.read_csv('datasets/super_bowls.csv')
tv         = pd.read_csv('datasets/tv.csv')
halftimeMusicians = pd.read_csv('datasets/halftime_musicians.csv')

# display sample data
print(superBowls.head(5))
print(tv.head(5))
print(halftimeMusicians.head(5))

# inspect tha data for missing values

# summary of tv data
print(tv.info())

print('/n')

# summary of halftime musician's data
print(halftimeMusicians.info())

# visually inspect super bowl data

# plot a histogram of combined points
superBowls.combined_pts.hist()
plt.xlabel('combined points')
plt.ylabel('number of super bowls')
plt.show()

# display the super bowls with the highest and lowest combined points
highest = superBowls[superBowls['combined_pts'] > 70]
lowest  = superBowls[superBowls['combined_pts'] < 25]

# beautify
#highest_message = 'Super Bowl ' + str(highest.super_bowls.iloc[0]) + 'had the highest combined points of ' + str(highest.combined_pts.iloc[0])
#print(highest_message)
#print()

# let us play around with point difference distribution

# plot a histogram of point differences
plt.hist(superBowls.difference_pts)
plt.xlabel('point difference')
plt.ylabel('number of super bowls')
plt.show()
