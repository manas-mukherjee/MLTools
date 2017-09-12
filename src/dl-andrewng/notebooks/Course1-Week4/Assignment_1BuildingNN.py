# GRADED FUNCTION: initialize_parameters_deep

import numpy as np

def initialize_parameters_deep(layer_dims):
    """
    Arguments:
    layer_dims -- python array (list) containing the dimensions of each layer in our network

    Returns:
    parameters -- python dictionary containing your parameters "W1", "b1", ..., "WL", "bL":
                    Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])
                    bl -- bias vector of shape (layer_dims[l], 1)
    """

    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)  # number of layers in the network
    print(L)
    for l in range(1, L):
        ### START CODE HERE ### ( 2 lines of code)
        parameters['W' + str(l)] = np.random.randn(layer_dims[1], layer_dims[0]) * 0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[1], 1))
        ### END CODE HERE ###

        assert (parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l - 1]))
        assert (parameters['b' + str(l)].shape == (layer_dims[l], 1))

    return parameters

# parameters = initialize_parameters_deep([5,4,3])
# print("W1 = " + str(parameters["W1"]))
# print("b1 = " + str(parameters["b1"]))
# print("W2 = " + str(parameters["W2"]))
# print("b2 = " + str(parameters["b2"]))

for l in range(1,5):
    print(l)

print('---------')
print(l)

l = [1,2,3,4,5]
print len(l)
print('---------')
L =2
for l in reversed(range(L-1)):
    print l
