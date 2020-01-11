

# alright well I am not a big fan nor a hater of the Kardashians and jenners
# the family polarization has an intriguing marketing prowess.
# say what you want about them but whatever they touch turns into content and eventul viral

# I will try to explore the data underneath the hype they create and find who is actually more famous

# I will use Google Trends data

# load the pandas
import pandas as pd
import matplotlib.pyplot as plt

# read the dataset
trends = pd.read_csv('datasets/trends_kj_sisters.csv')

# inspect a sample
print(trends.head())

# Numbers represent search interest relative to the highest point on the chart for the given region and time.
# A value of 100 is the peak popularity for the term.
# A value of 50 means that the term is half as popular.
# A score of 0 means there was not enough data for this term.
# well that is not straight foward

# first let us get some better column names
trends.columns = ['month', 'kim', 'khloe','kourtney','kendall','kylie']

# check
print(trends.tail())

# this '<' sign is going to be an issue
# check the info
print(trends.info())

# some columns are not integers becasue of '<' this thing
# let us remove it then change the type to int

# loop through the columns
for column in trends.columns :
    # only modify the columns that have '<'
    if '<' in trends[column].to_string():
        # remove the '<' and convert to int
        trends[column] = trends[column].str.replace('<','')
        trends[column] = pd.to_numeric(trends[column])

# check to see if miracle was done
#print(trends.info())
#print(trends.head())

# next convert month to type datetime
trends.month = pd.to_datetime(trends.month)

# inspect
#print(trends.info())
#print(trends.head())

# set month as indet
trends = trends.set_index('month')

# plot
trends.plot(title='Family trend')
plt.show()

# zoom in from January 2014 durying kylie's rise
trends.loc['2014-01':'2019-03'].plot(title="'Kylie's Rise Zoom")
plt.show()
