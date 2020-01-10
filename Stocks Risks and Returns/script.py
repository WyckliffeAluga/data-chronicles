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
