
import numpy
from scipy import stats
from sklearn import datasets, linear_model
import pandas 
import matplotlib.pyplot as plt
import os
import time
from dask import dataframe as dd
import csv

# Put this on the top

# for practice, uninstall numpy and scipy with pip

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

y = numpy.median(speed)
print(y)

z = stats.mode(speed)

print(z)

a = numpy.std(speed)

print("standard deviation is", a)

# Now for scatter plots

z
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


#df = pandas.read_csv('C:\\Users\\css7c\\Desktop\\Python_Programs\\NM_data.csv')


#print(df.to_string())

"""
# time taken to read data
s_time_dask = time.time()
dask_df = df1.read_csv('C:\\Users\\css7c\\Desktop\\Python_Programs\\data.csv')
e_time_dask = time.time()
print("Read with dask: ", (e_time_dask-s_time_dask), "seconds")

# data
dask_df.head(10)
"""

"""
# opening the CSV file 
with open('C:\\Users\\css7c\\Desktop\\Python_Programs\\NM_data.csv', mode ='r') as file:   
    # reading the CSV file 
    csvFile = csv.reader(file) 
"""

"""    
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        print(lines)
"""

filename = 'C:\\Users\\css7c\\Desktop\\Python_Programs\\NM_data.csv'
df = dd.read_csv(filename, dtype='str')

df.head(2)