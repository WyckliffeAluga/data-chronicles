# In this project I will be trying to analyze the volatility of cryptocurrency markets

# import modules
import pandas as pd
import matplotlib.pyplot as plt

# set the plot styling
plt.style.use('fivethirtyeight')

# read the most recent data from coinmarket API
current = pd.read_json('https://api.coinmarketcap.com/v1/ticker/')

# print out a sample
print(current.head(5))

# read and load 2017 market data from dataset
dec6 = pd.read_csv('datasets/coinmarketcap_06122017.csv')

# select the id and us market cap columns
market_cap_raw = dec6[['id','market_cap_usd']]

# count the number of values loaded
print(market_cap_raw.count())

# filter the rows without market capitalization data
cap = market_cap_raw.query('market_cap_usd > 0')

# coint again
print(cap.count())

# define some plotting variables
top_cap_title = 'Top 10 market capitalization'
top_cap_ylabel = '% of total capitalization'

# select the first 10 coins and set the index
cap10 = cap[:10].set_index('id')

# calculate the market capitalization percentage
cap10 = cap10.assign(market_cap_perc = lambda x:(x.market_cap_usd / cap.market_cap_usd.sum())*100)

# plot a bar plot
ax = cap10.plot(kind='bar', y='market_cap_perc', title=top_cap_title)

# set y label
ax.set_ylabel(top_cap_ylabel)
plt.show()

# lets add some colors and beautify
COLORS = ['orange', 'green', 'cyan','blue', 'silver', 'cyan', 'orange', 'red', 'green']

# replot again
ax = cap10.plot(kind='bar', y='market_cap_perc', title='top_cap_title', logy=True, color=COLORS)

# annotate
ax.set_xticklabels('')
ax.set_yticklabels('')
plt.show()

# study the volatility
# select id, daily percentage change, and weekly percentage change
volatility = dec6[['id','percent_change_24h','percent_change_7d']]

# set index to id
volatility = volatility.set_index('id')

# sort the data frame
volatility = volatility.sort_values('percent_change_24h', ascending=True)

# check a few samples
print(volatility.head(5))

# plot the top 10 biggest gainner and top 10 biggest losses

def top10plots(volatility_series, title):

    # mark the subplots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,6))

    # plot bottom 10 losers
    ax = (volatility_series[:10].plot.bar(color='darkred', ax=axes[0]))
    fig.suptitle(title)
    ax.set_ylabel('% change')

    # plot top 10 winners
    ax = (volatility_series[-10:].plot.bar(color='darkred', ax=axes[1]))

    # return fig and ax
    return fig, ax

dailyTitle = '24 hours biggest losers and winners'

# call the function for daily data
fig, ax = top10plots(volatility.percent_change_24h, dailyTitle)
plt.show()

# weekly volatility
volatility7d = volatility[['percent_change_7d']].sort_values('percent_change_7d', ascending=True)

# plot weekly volatily
weeklyTitle = 'Weekly top 10 losers and winners'
fig,ax = top10plots(volatility7d, weeklyTitle)
plt.show()

# check the marker sizes
# select everythin bigger than 10 bilion capitalization
largecaps = cap.query('market_cap_usd >= 10000000000')

# print out
print(largecaps)

# we can see most coins are very tiny
# categorize different capitalizations from caps

def capcount(query_string):
    return cap.query(query_string).count()

# create labels for the plots
labels = ['biggish', 'micro','nano']

# use cap count
# set the query strings
biggish_query = '(market_cap_usd > 10000000000) or (market_cap_usd > 2000000000 and market_cap_usd < 10000000000) or (market_cap_usd > 300000000 and market_cap_usd < 2000000000)'
micro_query ='market_cap_usd > 50000000 and market_cap_usd < 300000000'
nano_query = 'market_cap_usd < 50000000'

# use capcount
biggish = capcount(biggish_query)
micro   = capcount(micro_query)
nano    = capcount(nano_query)

# make a list of the 3 counts
values = [biggish, micro, nano]

# plot
plt.bar(range(len(values)), values)
plt.show()
