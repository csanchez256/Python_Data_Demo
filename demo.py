
import numpy
from scipy import stats
import pandas 
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os
import time
import csv


import dask.dataframe as dd
from dask.diagnostics import ProgressBar


"""
#This is useful if you just want to visually see the table elements
# But it can't infer data types
filename = '/Users/css/Desktop/Python Programs/Data/NM_data.csv'
df = dd.read_csv(filename, dtype='str')

# Print the first 10 rows from the data
x = df.head(10)

# Print the last two rows from the data
#print(df.tail(2))

"""

df = dd.read_csv('/Users/css/Desktop/Python Programs/Data/NM_data.csv')

#https://www.coiled.io/blog/dask-read-csv-to-dataframe
ddf = dd.read_csv('/Users/css/Desktop/Python Programs/Data/NM_data.csv', sample_rows=5000)
print(ddf.dtypes)



#Dask dataframes
# https://pnavaro.github.io/big-data/16-DaskDataframes.html


# How to run a regression with Pandas:  https://saturncloud.io/blog/how-to-run-an-ols-regression-with-pandas-data-frame/
data = pandas.read_csv('/Users/css/Desktop/Python Programs/Data/NM_data.csv', low_memory=False)
y = data['hhwt']
X = data[['perwt', 'hwsei']]
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
#print(model.summary())