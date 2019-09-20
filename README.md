# Money Flow Index
Data Wrangling/Manipulation Challenge - Data science

## Instructions

The money flow index (MFI) is a momentum indicator that measures the inflow and outflow of money into and out of a security over a specific period of time. It is computed as given below, and can assume values between 0 and 100.

Money Flow Index = 100 x Money Ratio/(1 + Money Ratio)

Money Ratio = Positive Money Flow Sum/Negative Money Flow Sum

Money Flow = Typical Price x Volume

Typical Price = (High Price + Low Price + Close Price)/3

The concepts of Positive and Negative are defined as follows: on any given day, the Money Flow is denoted positive / negative if the Typical Price is higher / lower than the previous day's typical price. If the Typical Price is unchanged then that day's data are discarded. The Positive Money Flow Sum is the sum of all the Positive Money Flow over a sliding window of n days. The Negative Money Flow Sum is the sum of all the Negative Money Flow over a sliding window of n days.

Given the stock price data consisting of open, close, volume, low and high price, calculate the Money Flow index for each day over a sliding window of n days(n will be given). The firs Money Flow Index value is calculated for the (n + 1)th day.

### Function Description
Complete the moneyFlowIndex function. The function must create a file money_flow_index_[n].csv containing the headers: Day, Open, High, Low, Close, Volume, Typical Price, Positive Money Flow, Negative Money Flow, Positive Money Flow Sum, Negative Money Flow Sum, and Money Flow Index as described in the example above. They money flow index should be calculated over a sliding window of n days, inclusive of the day for which it is calculated. No return value is expected

moneyFlowIndex has two parameters:
filename: a string describing the name of the input CSV file containing the headers: Day, Open, High, Low, Close, and Volume n: an integer

### Evaluation
The output file must meet the following conditions:
1. The output CSV file must contain the headers in the given order: Day, Open, High, Low, Close, Volume, Typical Price, Positive Money Flow, Negative Money Flow, Positive Money Flow Sum, Negative Money Flow Sum, and Money Flow Index.
2. The Day, Open, High, Low, Close, and Volume must exactly match with the values given in the input of CSV file.
3. The computed values of Typical Price, Positive Money Flow, Negative Money Flow, Positive Money Flow Sum, Negative Money Flow Sum and Money Flow Index value should not deviate from the correct values by more than 10-6.

