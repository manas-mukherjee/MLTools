import numpy as np

if False:
    x = np.array([[0,3,4],[2,6,4],[7,8,9],[1,2,3]])
    print x
    #print x.T
    #print x.reshape(x.shape[0]*x.shape[1],1)
    #x_norm = np.linalg.norm(x,axis=1,keepdims=True)
    #print x/x_norm

    print x.reshape(2,-1)
if False:
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

if False:
    x = np.array([[[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]], [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]],
                  [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]]])
    #print x
    #print x.shape

    print '--------------------'
    x = np.array([[[[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]], [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]],
                  [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]]],
                 [[[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]], [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]],
                  [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]]],
                 [[[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]], [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]],
                  [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]]],
                 [[[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]], [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]],
                  [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]]],
                 [[[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]], [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]],
                  [[0, 1, 2, 9], [3, 4, 5, 1], [6, 7, 8, 5]]]
                  ]
                 )
    print x
    print x.shape
    print x.shape[0],x.shape[1],x.shape[2],x.shape[3]
    print '------------------------------------------'
    input = x.reshape(x.shape[0], -1).T
    print input
    print input.shape
    print input[:,0]
    print input[2,:]

if False:
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    w, b, X, Y = np.array([[1], [2]]), 2, np.array([[1, 2], [3, 4]]), np.array([[1, 0]])
    print 'w shape - ', w.shape
    print 'w  - ', w.shape
    print 'X - ', X.shape
    print b
    print Y

    print ('np.dot(w.T,X)')
    z = np.dot(w.T,X) + b
    print z

    print ('A = sigmoid(z)')
    print sigmoid(z)[0][0], sigmoid(z)[0][1]

    m = X.shape[1]
    print ('m', m)

    test = (np.log(sigmoid(z)[0][0]) + np.log(1-sigmoid(z)[0][1]))
    print 'test - ', test

if True:
    A = np.array([[ 0.99987661,  0.99999386]])
    B = np.array([ 0.99987661,  0.99999386])

    print A.shape, B.shape