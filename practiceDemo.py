import numpy 
import dask.dataframe as dd
from scipy import stats

age = [18,22,46,86,23,55,66,77,12,22,14,10]

x = numpy.median(age)
mean = numpy.mean(age)
s = numpy.std(age)

print("The median is", x)
print("The mean is", mean)
print("The standard deviation is", s)

# now scipy
#mode = stats.mode(age)

#print("the mode is", mode)

#This is useful if you just want to visually see the table elements
# But it can't infer data types
filename = '/Users/css/Desktop/Python Programs/Python_Data_Demo/Data/NM_data.csv'
df = dd.read_csv(filename, dtype='str')

# Print the first 10 rows from the data
x = df.head(10)

#print("the first 10 records are", x)
# Print the last two rows from the data
#print(df.tail(2))