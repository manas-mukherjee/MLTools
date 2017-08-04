import pandas
import numpy

# Read the data
data = pandas.read_csv('data.csv')

# Split the data into X and y
X = numpy.array(data[['x1', 'x2']])
y = numpy.array(data['y'])

# Import the SVM Classifier
from sklearn.svm import SVC

# TODO: Define your classifier.
# Play with different values for these, from the options above.
# Hit 'Test Run' to see how the classifier fit your data.
# Once you can correctly classify all the points, hit 'Submit'.
# classifier = SVC(kernel = 'poly', degree = 2, gamma = None, C = None)
classifier = SVC(kernel = 'poly', degree = 2)
# ideal - classifier = SVC(kernel = 'rbf', degree = 2,  gamma = 200)
#TODO : Learn more on the SVM variables

# Fit the classifier
classifier.fit(X,y)