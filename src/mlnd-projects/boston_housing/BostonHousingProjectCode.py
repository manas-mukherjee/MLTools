# Import libraries necessary for this project
import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split

#Import 'make_scorer', 'DecisionTreeRegressor', and 'GridSearchCV'
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer
from sklearn.grid_search import GridSearchCV

# Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)

# Success
print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)

# Stats
if True:
    minimum_price = np.min(prices)
    maximum_price = np.max(prices)
    mean_price = np.mean(prices)
    median_price = np.median(prices)
    std_price = np.std(prices)

    # Show the calculated statistics
    print "Statistics for Boston housing dataset:\n"
    print "Minimum price: ${:,.2f}".format(minimum_price)
    print "Maximum price: ${:,.2f}".format(maximum_price)
    print "Mean price: ${:,.2f}".format(mean_price)
    print "Median price ${:,.2f}".format(median_price)
    print "Standard deviation of prices: ${:,.2f}".format(std_price)

    print data[(data.RM > 4.5) & (data.RM <5.5 )]

    print "Mean price of housing with 5 bedroom - " , np.mean(data[data['RM']==5]['MEDV'])


def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between
        true and predicted values based on the metric chosen. """

    return r2_score(y_true, y_predict)

# Splitting data-set
X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size = 0.20)
print "Training and testing split was successful."


def fit_model(X, y):
    """ Performs grid search over the 'max_depth' parameter for a
        decision tree regressor trained on the input data [X, y]. """

    # Create cross-validation sets from the training data
    # sklearn version 0.18: ShuffleSplit(n_splits=10, test_size=0.1, train_size=None, random_state=None)
    # sklearn versiin 0.17: ShuffleSplit(n, n_iter=10, test_size=0.1, train_size=None, random_state=None)
    cv_sets = ShuffleSplit(X.shape[0], n_iter=10, test_size=0.20, random_state=0)

    regressor = DecisionTreeRegressor()

    params = {'max_depth': list(range(1, 11))}

    scoring_fnc = make_scorer(performance_metric)

    grid = GridSearchCV(estimator=regressor, param_grid=params, scoring=scoring_fnc, cv=cv_sets)

    grid = grid.fit(X, y)

    return grid.best_estimator_

# Fit the training data to the model using grid search
reg = fit_model(X_train, y_train)

# Produce the value for 'max_depth'
print "Parameter 'max_depth' is {} for the optimal model.".format(reg.get_params()['max_depth'])

# Produce a matrix for client data
client_data = [[5, 17, 15],  # Client 1
               [4, 32, 22],  # Client 2
               [8, 3, 12]]  # Client 3

# Show predictions
for i, price in enumerate(reg.predict(client_data)):
    print "Predicted selling price for Client {}'s home: ${:,.2f}".format(i + 1, price)


