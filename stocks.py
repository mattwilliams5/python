#!/usr/bin/python

import pandas as pd
#from pandas_datareader import data as web
import pandas_datareader.data as web
import datetime


# creating start and stop times for our stock
start = datetime.datetime(2016,1,1)
end = datetime.date.today()


#Retrieving user input for historical data or quotes for stock

ans = input("Enter 1 for historical data or 2 for quote: ")

if ans == 1:
    stock = raw_input("Please enter the stock you want historical data from: ")
    hist = web.DataReader(stock, 'google', start, end)
    print(hist)
elif ans == 2:
    quote = raw_input("Please enter the stock you want todays quote from: ")
    q = web.get_quote_google([quote, 'GOOG'])
    print(q)


#print(f)
#q = web.get_quote_google(['AMZN', 'GOOG'])

#print(q)
