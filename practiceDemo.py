import numpy 
from scipy import stats #for mode and regression
import matplotlib.pyplot as plot
import dask.dataframe as dd #for reading in large file


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



########################
# Simple scatter plot  #
########################

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plot.scatter(x, y)
plot.plot(x, mymodel)
plot.show()


########################
# Read in a large file #
########################

#This is useful if you just want to visually see the table elements
# But it can't infer data types
filename = '/Users/css/Desktop/Python Programs/Python_Data_Demo/Data/NM_data.csv'
df = dd.read_csv(filename, dtype='str')

# Print the first 10 rows from the data
x = df.head(10)

print("the first 10 records are", x)
# Print the last two rows from the data
#print(df.tail(2))