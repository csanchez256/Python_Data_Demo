
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
filename = '/Users/css/Desktop/Python Programs/Python_Data_Demo/Data/NM_data.csv'
df = dd.read_csv(filename, dtype='str')

# Print the first 10 rows from the data
x = df.head(10)

# Print the last two rows from the data
#print(df.tail(2))

"""

filename = '/Users/css/Desktop/Python Programs/Python_Data_Demo/Data/NM_data.csv'
df = dd.read_csv(filename, dtype='str')

# Print the first 10 rows from the data
x = df.head(10)

print(x)