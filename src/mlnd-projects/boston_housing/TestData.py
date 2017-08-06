# Import libraries necessary for this project
import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit

# Import supplementary visualizations code visuals.py
# import visuals as vs

# Pretty display for notebooks
# %matplotlib inline

# Load the Boston housing dataset
'''
'RM' is the average number of rooms among homes in the neighborhood.
'LSTAT' is the percentage of homeowners in the neighborhood considered "lower class" (working poor).
'PTRATIO' is the ratio of students to teachers in primary and secondary schools in the neighborhood.
'''
data = pd.read_csv('housing.csv')
prices = data['MEDV']

print 'min', np.min(prices)
print 'max', np.max(prices)
print 'mean', np.mean(prices)
print 'median', np.median(prices)
print 'std. deviation', np.std(prices)

print "Standard deviation of prices: ${:,.2f}".format(np.std(prices))

print data.head(10)
print np.max(data['LSTAT'])
print data[data['LSTAT']>20]