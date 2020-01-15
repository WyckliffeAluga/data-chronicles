Overview 

Use pandas to calculate and compare profitability and risk of different investments using the Sharpe Ratio.

Description

When you assess whether to invest in an asset, 
you want to look not only at how much money you could make but also at how much risk you are taking. 
The Sharpe Ratio, developed by Nobel Prize winner William Sharpe some 50 years ago, does precisely this:
it compares the return of an investment to that of an alternative and relates the relative return to the risk of the investment, 
measured by the standard deviation of returns.

Meet Professor William Sharpe

An investment may make sense if we expect it to return more money than it costs. 
But returns are only part of the story because they are risky - there may be a range of possible outcomes. 
How does one compare different investments that may deliver similar results on average, but exhibit different levels of risks?

Enter William Sharpe.

He introduced the reward-to-variability ratio in 1966 that soon came to be called the Sharpe Ratio. 
It compares the expected returns for two investment opportunities and calculates the additional 
return per unit of risk an investor could obtain by choosing one over the other.
In particular, it looks at the difference in returns for two investments and compares 
the average difference to the standard deviation (as a measure of risk) of this difference.
A higher Sharpe ratio means that the reward will be higher for a given amount of risk. 
It is common to compare a specific opportunity against a benchmark that represents an entire category of investments.

The Sharpe ratio has been one of the most popular risk/return measures in finance, not least because it's so simple to use. 
It also helped that Professor Sharpe won a Nobel Memorial Prize in Economics in 1990 for his work on the capital asset pricing model (CAPM).

The Sharpe ratio is usually calculated for a portfolio and uses the risk-free interest rate as benchmark. 
In this project I will simplify the example and use stocks instead of a portfolio. 
I will also use a stock index as benchmark rather than the risk-free interest rate because both are 
readily available at daily frequencies and I do not have to get into converting interest rates from annual to daily frequency.

I will use Sharpe ratio by calculating it for the stocks of the two tech giants Facebook and Amazon.
As benchmark I'll use the S&P 500 that measures the performance of the 500 largest stocks in the US. 
When a stock index is used instead of the risk-free rate, the result is called the Information Ratio and 
is used to benchmark the return on active portfolio management because it tells you
how much more return for a given unit of risk your portfolio manager earned relative to
just putting your money into a low-cost index fund.

