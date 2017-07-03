#!/usr/bin/python

import pandas as pd
import pandas_datareader.data as web
import datetime
from pandas_datareader.data import Options
from pandas_datareader import wb

# creating start and stop times for our stock
start = datetime.datetime(2016,1,1)
end = datetime.date.today()


#Retrieving user input for historical data or quotes for stock

ans = input("Enter 1 for historical data, 2 for quote or 3 for options: ")

if ans == 1:
    stock = raw_input("Please enter the stock you want historical data from: ")
    hist = web.DataReader(stock, 'google', start, end)
    print(hist)
elif ans == 2:
    quote = raw_input("Please enter the stock you want todays quote from: ")
    q = web.get_quote_google([quote, 'GOOG'])
    print(q)
elif ans == 3:
    opts = raw_input("Please enter stock you need options results for: ")
    go_opts = Options(opts, 'google')
    data = go_opts.get_options_data(expiry=go_opts.expiry_dates[0])
    print(data.iloc[0:5, 0:5])
