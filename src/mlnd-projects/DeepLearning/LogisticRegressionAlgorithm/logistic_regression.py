import numpy as np

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


def prediction(X, W, b):
    return sigmoid(np.matmul(X, W) + b)


def error_vector(y, y_hat):
    return [-y[i] * np.log(y_hat[i]) - (1 - y[i]) * np.log(1 - y_hat[i]) for i in range(len(y))]


def error(y, y_hat):
    ev = error_vector(y, y_hat)
    return sum(ev) / len(ev)


# TODO: Fill in the code below to calculate the gradient of the error function.
# The result should be a list of three lists:
# The first list should contain the gradient (partial derivatives) with respect to w1
# The second list should contain the gradient (partial derivatives) with respect to w2
# The third list should contain the gradient (partial derivatives) with respect to b
def dErrors(X, y, y_hat):
    DErrorsDx1 = []
    DErrorsDx2 = []
    DErrorsDb = []

    for xi, yi, yi_hat in zip(X, y, y_hat):
        DErrorsDx1.append(-(yi - yi_hat) * xi[0])
        DErrorsDx2.append(-(yi - yi_hat) * xi[1])
        DErrorsDb.append(-(yi - yi_hat))

    # print DErrorsDx1, DErrorsDx2, DErrorsDb
    return DErrorsDx1, DErrorsDx2, DErrorsDb


# TODO: Fill in the code below to implement the gradient descent step.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b.
# It should calculate the prediction, the gradients, and use them to
# update the weights and bias W, b. Then return W and b.
# The error e will be calculated and returned for you, for plotting purposes.

'''
So think of it like this. If you had 100 records and you were using these 100 records you could do the following:

You could find the error for each record change the weight immediately and do this for all the 100 records.
You could find the errors for each record but instead of changing the weight immediately just accumulate the weight changes and then after all the 100 records are done change the weight.
What is the difference between the two? Would you get the same result in both the cases?
Ref - https://discussions.udacity.com/t/logistic-regression-algorithm-derivative-of-error-function/404081/9
'''

def gradientDescentStep(X, y, W, b, learn_rate=0.01):
    # TODO: Calculate the prediction
    # TODO: Calculate the gradient
    # TODO: Update the weights
    # This calculates the error

    m = len(X)
    # learn_rate = learn_rate/m

    y_hat = prediction(X, W, b)
    DErrorsDx1, DErrorsDx2, DErrorsDb = dErrors(X, y, y_hat)

    W[0] = W[0] - learn_rate * sum(DErrorsDx1)
    W[1] = W[1] - learn_rate * sum(DErrorsDx2)

    b = b - learn_rate * sum(DErrorsDb)

    e = error(y, y_hat)

    return W, b, sum(e)


# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainLR(X, y, learn_rate=0.01, num_epochs=100):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    # Initialize the weights randomly
    W = np.array(np.random.rand(2, 1)) * 2 - 1
    b = np.random.rand(1)[0] * 2 - 1
    # These are the solution lines that get plotted below.
    boundary_lines = []
    errors = []
    for i in range(num_epochs):
        # In each epoch, we apply the gradient descent step.
        W, b, error = gradientDescentStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0] / W[1], -b / W[1]))
        errors.append(error)
    return boundary_lines, errors
