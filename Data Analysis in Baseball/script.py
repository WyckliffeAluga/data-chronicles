
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
judge.tail()
