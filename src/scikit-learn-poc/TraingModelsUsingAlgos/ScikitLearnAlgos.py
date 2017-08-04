import pandas
import numpy

# Read the data
data = pandas.read_csv('data.csv')

# Split the data into X and y
X = numpy.array(data[['x1', 'x2']])
y = numpy.array(data['y'])

# import statements for the classification algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

# TODO: Pick an algorithm from the list:
# - Logistic Regression
# - Decision Trees
# - Support Vector Machines
# Define a classifier (bonus: Specify some parameters!)
# and use it to fit the data
# Click on `Test Run` to see how your algorithm fit the data!

# Logistic Regression Classifier
classifier = LogisticRegression()
classifier.fit(X,y)

# Decision Tree Classifier
classifier = GradientBoostingClassifier()
classifier.fit(X,y)

# Support Vector Machine Classifier
classifier = SVC()
classifier.fit(X,y)

# TODO: Couldn't test this as it is supported only scikit-learn 0.18 onwords
# Neural Network
# from sklearn.neural_network import MLPClassifier
# classifier = MLPClassifier()