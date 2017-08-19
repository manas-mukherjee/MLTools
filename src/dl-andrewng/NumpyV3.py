import numpy as np

if False:
    x = np.array([[0,3,4],[2,6,4]])
    print x
    x_norm = np.linalg.norm(x,axis=1,keepdims=True)
    print x/x_norm


if True:
    def L2(yhat, y):
        """
        Arguments:
        yhat -- vector of size m (predicted labels)
        y -- vector of size m (true labels)

        Returns:
        loss -- the value of the L2 loss function defined above
        """

        loss = np.dot((y - yhat),(y - yhat))

        ### END CODE HERE ###

        return loss


    yhat = np.array([.9, 0.2, 0.1, .4, .9])
    y = np.array([1, 0, 0, 1, 1])
    print("L2 = " + str(L2(yhat, y)))
