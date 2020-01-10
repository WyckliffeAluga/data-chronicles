# Use sharpe ration to meausure risk/return in stock market
# use S & P 500 as benchmark to analyze amazon and facebook

# import some modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set the styling of the plots
plt.style.use('fivethirtyeight')

# read in the data
stockData = pd.read_csv('datasets/stock_data.csv',
                        parse_dates=['Date'],
                        index_col='Date').dropna()

benchmarkData = pd.read_csv('datasets/benchmark_data.csv',
                        parse_dates=['Date'],
                        index_col='Date').dropna()

# display the summary of the stocks data
print('Stocks\n')
print(stockData.info())
print(stockData.head(5))

# display the summary of the benchmark data
print('\nBenchmarks\n')
print(benchmarkData.info())
print(benchmarkData.head(5))

# visualize the stock data
stockData.plot(subplots=True, title='Stock Data')
plt.show()
# print summary
print(stockData.describe())

# visualize the benchmark data
benchmarkData.plot(title='S&P 500')
plt.show()
# print the summary
print(benchmarkData.describe())

# prepare inputs for the Sharpe Ratio

# calculate daily stock returns
stock_returns = stockData.pct_change()

# visualize
stock_returns.plot(title='Daily Stock Returns')
plt.show()

# print out the summary
print(stock_returns.describe())

# calculate daily benchmark data returns
sp_returns = benchmarkData['S&P 500'].pct_change()

# visualize it
sp_returns.plot(title='S & P 500 daily returns')
plt.show()

# print out the summary
print(sp_returns.describe())

# calculate the difference in daily returns
excess_returns = stock_returns.sub(sp_returns,axis=0)

# visualize
excess_returns.plot(title='Excess returns')
plt.show()

# print summary
print(excess_returns.describe())

# STEP 1 : The average difference in daily Returns
# calculate the mean of excess returns
avg_excess_return = excess_returns.mean()

# visualize
avg_excess_return.plot(kind='bar', title='Mean of the return differences')
plt.show()

# STEP 2: standard deviation of the return difference
# calculate the stds
sd_excess_return = excess_returns.std()

# visualize
sd_excess_return.plot(kind='bar', title='Standard Deviation of the return differences')
plt.show()

# all together nwo
# calculate the daily sharpe ration
daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)

# annualize the sharpe ratio
annual_factor = np.sqrt(252)
annual_sharpe_ratio = daily_sharpe_ratio.mul(annual_factor)

# visualize
annual_sharpe_ratio.plot(kind='bar', title='Annualized sharpe ratio: Stocks vs S&P 500')
plt.show()
