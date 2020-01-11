
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


# analyze home runs
# filter homeruns only
judge_hr = judge[judge['events'] == 'home_run']
stanton_hr = stanton[stanton['events'] == 'home_run']

# plot it out
fig1, axs1 = plt.subplots(ncols=2, sharex=True, sharey=True)
sns.regplot(x='launch_speed', y='launch_angle', fit_reg=False, color='tab:blue', data=judge_hr, ax=axs1[0]).set_title('Aaron Judge\nHome Runs, 2015-2017')
sns.regplot(x='launch_speed', y='launch_angle', fit_reg=False, color='tab:blue', data=stanton_hr, ax=axs1[1]).set_title('Giancarlo Stanton\nHome Runs, 2015-2017')
plt.show()

# KDE plots of launch speed vs. launch angle, one for each player's home runs
fig2, axs2 = plt.subplots(ncols=2, sharex=True, sharey=True)
sns.kdeplot(judge_hr.launch_speed, judge_hr.launch_angle, cmap="Blues", shade=True, shade_lowest=False, ax=axs2[0]).set_title('Aaron Judge\nHome Runs, 2015-2017')
sns.kdeplot(judge_hr.launch_speed, judge_hr.launch_angle, cmap="Blues", shade=True, shade_lowest=False, ax=axs2[1]).set_title('Giancarlo Stanton\nHome Runs, 2015-2017')
plt.show()

# let us analyze home runs by pitch velocity

# combine data for thr two sluggers

judge_stanton_hr = pd.concat([judge_hr, stanton_hr])

# create a box plot to describe the pitc velocity
sns.boxplot('player_name','release_speed',data=judge_stanton_hr, color='blue' ).set_title('Home Runs, 2015-2017')
plt.show()

# home runs by pickt location

# define a function to assign x coordingate from Statcast data

def assign_x_coord(row):
    """
    Assigns an x-coordinate to Statcast's strike zone numbers. Zones 11, 12, 13,
    and 14 are ignored for plotting simplicity.
    """
    # left third of strik zone
    if row.zone in [1,4,7]:
        return 1

    # middle third of strike zone
    if row.zone in [2,5,8]:
        return 2

    # right third of strike zone
    if row.zone in [3,6,9]:
        return 3

# define a function to assign y coordinates

def assign_y_coord(row):
    """
    Assigns a y-coordinate to Statcast's strike zone numbers. Zones 11, 12, 13,
    and 14 are ignored for plotting simplicity.
    """
    # upper third of strike zone
    if row.zone in [1,2,3]:
        return 3

    # middle third of strike zone
    if row.zone in [4,5,6]:
        return 2

    # lower third of strike zone
    if row.zone in [7,8,9]:
        return 1

# assign cartesian coordinates to pitches
judge_strike_hr = judge_hr.copy().loc[judge_hr.zone <= 9]

judge_strike_hr['zone_x'] = judge_strike_hr.apply(assign_x_coord, axis=1)
judge_strike_hr['zone_y'] = judge_strike_hr.apply(assign_y_coord, axis=1)

plt.hist2d(judge_strike_hr.zone_x, judge_strike_hr.zone_y, bins = 3, cmap='Blues')
plt.title('Aaron Judge Home Runs on\n Pitches in the Strike Zone, 2015-2017')
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
cb = plt.colorbar()
cb.set_label('Counts in Bin')
plt.show()

stanton_strike_hr = stanton_hr.copy().loc[stanton_hr.zone <=9]

stanton_strike_hr['zone_x'] = stanton_strike_hr.apply(assign_x_coord, axis=1)
stanton_strike_hr['zone_y'] = stanton_strike_hr.apply(assign_y_coord, axis=1)

plt.hist2d(stanton_strike_hr.zone_x, stanton_strike_hr.zone_y, bins = 3, cmap='Blues')

plt.title('Giancarlo Stanton Home Runs on\n Pitches in the Strike Zone, 2015-2017')
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
cb = plt.colorbar()
cb.set_label('Counts in Bin')
plt.show()
