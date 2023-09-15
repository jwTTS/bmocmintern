# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:44:22 2023

@author: wilkijam
"""

#%% Functions in Python

# def functionName(argu1, argu2, ....):
    # code to run when the function is called
    # [OPTIONAL: 
    # return whatYouWantToReturn]
    
# Create a function that gets you the square of a number

def fnSquare(num):
    sqNum = num ** 2
    print(sqNum)
    return sqNum

fnSquare(3) + 5

#%% Numpy library

# Common uses for numpy:
    # 1) Constant retrieval
    # 2) Random number generator
    # 3) Matrix
    # 4) Stats functions
    
# Recreates some of the functionality in MATLAB or SPSS

# Packages - must be installed in order to import into your code
    # this is where anaconda makes life easier
# Packages must be imported into your code to take advantage of them

import numpy as np

# Random number generation (randint)
print(np.random.randint(1, 7, 1, int))

# Remember that no number is truly random in these examples
# We can provide a seed to our number generator, to force the same result for
# others

np.random.seed(12)
np.random.random(10)

# Random normal distribution
np.random.normal()

# Numpy is tremendously well set up for matrix math.
# It is INCREDIBLY well optimized.

# Numpy for statistics
data = np.random.normal(5, 2, 10000)

print(np.mean(data))
print(np.sum(data))
print(np.std(data))

#%% Pandas in Python

# pandas -> python data analysis library

# it is very popular because it has a LOT of similarities to Excel
    # Pandas uses objects called data frames
    # A dataframe is a collection of series'
    # A series is essentially a column

# Why uses pandas instead of Excel?
    # Extremely repeatable
    # Way faster
    # Can handle Way more data
    
# It is not the amazing Excel replacement:
    # Most people know nothing about Python
    # Excel is good for quick & dirty analysis

# Info you should know about pandas
    # How do we import pandas and data to use
    # Reviewing / preparing
    # Access data
    # Exporting (to csv, to json...)
    # Working with your data
        # sorting
        # creating calculated columns
        # filtering
        # combinations
    # Plotting data
    
# Importing the pandas package
import pandas as pd

# Importing data for pandas to work with
sp500 = pd.read_csv('StockData/SP500.csv')

sp500 = pd.read_csv('C:/Users/wilkijam/Downloads/Marquee-Python-1-Files-Sep-2023/Python Project/StockData/SP500.csv')

# Common issues on pandas data import:
    # If you get 'name is not defined' is that you didn't import pandas properly
    # If you get no such file or directory: it can't find your file, 
    # double check the location and double check that the file isn't open
    
# Exploring a pandas dataframe
# Check the first few or last few rows
sp500.head()
sp500.head(12)

sp500.tail()
sp500.tail(12)

sp500.info()
# This will give you an overview of data types and the number of non-blank
# records

sp500.describe()
# Quick statistical overview of your data set

# Importing Data from Excel
# Use pd.read_excel

finData = pd.read_excel('ExData/Data Manipulation Worksheet.xlsx')
# Read excel defaults to the first tab in a file

finData = pd.read_excel('ExData/Data Manipulation Worksheet.xlsx',
                        sheet_name='Financing Table Clean')


# Read_HTML allows you to read a website of data

ipos = pd.read_html('https://www.iposcoop.com/last-100-ipos/')

# Accessing data in pandar
    # Access a column
    # a row
    # a slice
    # a single data point
    # Export data somewhere else
    
# Accessing columns
    # Accessing a single column, use the header

'use bracket notation'
sp500['Volume']
# or use dot notation
sp500.Volume

# dot notation doesn't work with spaces / special characters
sp500.Adj Close

# Use lists to get multiple columns
sp500[['Close', 'Volume']]

# Converting dates to datetime values
sp500 = pd.read_csv('StockData/SP500.csv', parse_dates=['Date'])
sp500.info()

# Can also do this after import
sp500 = pd.read_csv('StockData/SP500.csv')
sp500['Date'] = pd.to_datetime(sp500['Date'])

# Change the index to be the date column
sp500 = sp500.set_index(['Date'])
# Can do this while reading
sp500 = pd.read_csv('StockData/SP500.csv', index_col=0)

# Accessing rows in pandas
    # 1) .iloc[] -> use the default indices assigned
        # df.iloc[x] -> gets me row x
        # df.iloc[x:y] -> gets me from row x to row y-1
    # 2) .loc[] -> use the "fancy" index created

sp500.iloc[3]
sp500.loc['2013-10-04']
sp500.loc['20131004']
# when you have dates as your index you can get a lot smarter with your
# slicing using .loc
sp500.loc['2013-10']

# Can use combination of .loc or .iloc and column name
sp500.loc['2013.10']['Close']

sp500.loc['2013-10-04']['Close']

# Exporting data from pandas
sp500.to_csv('Output/My CSV Output.csv')
sp500.to_excel('Output/My XL Output.xlsx')
