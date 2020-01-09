
# hi
# in this project I will try to analyze tv data to answer questions like
# What are the most extreme outcomes in super bowl
# How does the game affect tv viewership
# how have viewership , TV ratings and ad cost evolved over time
# Who is the most prolific musician in terms of half time perfomances

# import modules

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# display the closest games and biggest blowouts
print(superBowls[superBowls['difference_pts'] == 1])
print(superBowls[superBowls['difference_pts'] >= 35])


# do blowouts translate to lost viewership?

# join game and TV data, then filter out SB I because it was split over two networks
gamesTv = pd.merge(tv.query('super_bowl > 1') , superBowls , on='super_bowl')

# create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=gamesTv)
plt.show()

# viewership and ad industry over times

# create a figure with 3 x 1 subplot
plt.subplot(3, 1,1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average number of US viewers')

# middle plot
plt.subplot(3,1,2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household ratings')

# activate the bottom plot
plt.subplot(3,1,3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('Super Bowl')

# nice spacing
plt.tight_layout()
plt.show()

# let us go to music

# count the halftime show perfomances for each musician and sort by apperances
halftime_appearances = halftimeMusicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl' , ascending=False)

# musicians with more than one halftime apperances
print(halftime_appearances[halftime_appearances['super_bowl'] > 1])

# Who performed the most

# filter out the bands
no_bands = halftimeMusicians[~halftimeMusicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# plot a histogram
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.ylabel('Number of musicians')
plt.show()

# sort the non-band musicians
no_bands = no_bands.sort_values('num_songs', ascending=False)
print(no_bands.head(10))
