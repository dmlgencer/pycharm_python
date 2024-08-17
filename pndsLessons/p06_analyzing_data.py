

import pandas as pd

'''
Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top.

'''
df = pd.read_csv('data.csv')

print(df.head(10))

'''
In our examples we will be using a CSV file called 'data.csv'.

Download data.csv, or open data.csv in your browser.

Note: if the number of rows is not specified, the head() method will return the top 5 rows.
'''
df = pd.read_csv('data.csv')

print(df.head())

'''
There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom.'''
print(df.tail())

'''Info About the Data
The DataFrames object has a method called info(), that gives you more information about the data set.'''

print(df.info())


