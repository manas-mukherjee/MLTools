# Reading the csv file
import pandas as pd
data = pd.read_csv("data.csv")

# Splitting the data into X and y
import numpy as np
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

# Import statement for train_test_split
from sklearn.cross_validation import train_test_split

'''
Splitting a dataset into training and testing data is very easy with sklearn. 
All we need is the command train_test_split. The function takes as inputs X and y, and returns four things:

X_train: The training input
X_test: The testing input
y_train: The training labels
y_test: The testing labels
'''

# TODO: Use the train_test_split function to split the data into
# training and testing sets.
# The size of the testing set should be 20% of the total size of the data.
# Your output should contain 4 objects.


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

print len(X)
print len(X_train)
print len(X_test)