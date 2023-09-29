
import numpy
from scipy import stats
import pandas 
import matplotlib.pyplot as plt
import os
import time
import csv


import dask.dataframe as dd
from dask.diagnostics import ProgressBar

# Put this on the top

# for practice, uninstall numpy and scipy with pip

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

y = numpy.median(speed)
print("Median is ", y)

#z = stats.mode(speed)

#print("Mode is ", z)

a = numpy.std(speed)

print("standard deviation is", a)

# Now for scatter plots


x = [5,7,8,7,2,17,2,9,4,11,12]
y = [99,86,87,88,86,87,94,78,77,85,86]

#plt.scatter(x, y)
#plt.show()

# from sklearn import datasets, linear_model
# Throws error
# pip install scikit-learn

cwd = os.getcwd()
files = os.listdir(cwd)
print("files in %r" % (cwd))

# If you're running windows your path may look something like this
#df = pandas.read_csv('C:\\Users\\css7c\\Desktop\\Python_Programs\\NM_data.csv')


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



#Dask dataframes
# https://pnavaro.github.io/big-data/16-DaskDataframes.html

