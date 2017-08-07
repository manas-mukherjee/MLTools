'''

Scikit-learn is an open source Machine Learning library that is built on NumPy, SciPy and matplotlib.
It uses a Python interface and supports various regression, classification and clustering algorithms.
'''

''' install sklearn with the command: pip install scikit-learn or conda install scikit-learn '''

from sklearn import datasets # sklearn comes with a variety of preloaded datasets
from sklearn import metrics # calculate how well our model is doing
from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer
from sklearn.grid_search import GridSearchCV

'''conda -c install scikit-learn=0.17'''

# Load the dataset
housing_data = datasets.load_boston()

# Define model
linear_regression_model = LinearRegression()

# Here, housing_data.data is our feature set and housing_data.target are the labels we are trying to predict.
linear_regression_model.fit(housing_data.data, housing_data.target)

predictions = linear_regression_model.predict(housing_data.data)

# Measure - Since this is a regression problem, we will use the r2 score metric.
score = metrics.r2_score(housing_data.target, predictions)

print score

