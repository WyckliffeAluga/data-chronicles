

# alright well I am not a big fan nor a hater of the Kardashians and jenners
# the family polarization has an intriguing marketing prowess.
# say what you want about them but whatever they touch turns into content and eventul viral

# I will try to explore the data underneath the hype they create and find who is actually more famous

# I will use Google Trends data

# load the pandas
import pandas as pd

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
print(trends.head())
