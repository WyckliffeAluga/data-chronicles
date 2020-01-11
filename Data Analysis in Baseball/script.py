
# here we go
# in this prokect
# I will Use MLB's Statcast data to compare New York Yankees sluggers Aaron Judge and Giancarlo Stanton.

# Statcast is a state-of-the-art tracking system that uses high-resolution cameras and radar equipment to measure the precise location and movement of baseballs and baseball players.
# Introduced in 2015 to all 30 major league ballparks, Statcast data is revolutionizing the game.

# Here I am going to wrangle , visualize and visualize Statcast data to compare two key players

# import some modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# laod Aaron Judge's data
judge = pd.read_csv('datasets/judge.csv')

# load Giancarlo Stanton's data
stanton = pd.read_csv('datasets/stanton.csv')

# display all the columbns
pd.set_option('display.max_columns', None)

# display the last five rows of Jude's file
#print(judge.tail())

# let us dig in then

# All of Judge;s batted ball event in 2017
judge_events_2017 = judge.loc[judge['game_year'] == 2017].events
print("Aaron Judge batted ball event totals, 2017:")
print(judge_events_2017.value_counts())

# all of Stanton's batted ball events in 2017
stanton_events_2017 = stanton.loc[stanton['game_year'] == 2017].events
print("\nGiancarlo Stanton batted ball event totals, 2017:")
print(stanton_events_2017.value_counts())
