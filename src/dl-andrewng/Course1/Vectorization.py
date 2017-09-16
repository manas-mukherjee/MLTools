import numpy as np
import time
import math

if False:
    a = np.random.rand(10)
    b = np.random.rand(10)

    tic = time.time()
    c = np.dot(a, b)
    toe = time.time()

    print c
    print "Vectorized version: ", str(1000 * (toe - tic))

    c = 0
    tic = time.time()
    for i in range(10):
        c += a[i] * b[i]
    toe = time.time()

    print c
    print "Loop version: ", str(1000 * (toe - tic))

if False:
    n = 10
    u = np.zeros((n,1))
    v = np.zeros((n,1))

    for i in range(n):
        u[i] = math.exp(i)
        v[i] = np.exp(i)

    print u,v

if True:
    a = np.random.randn(2, 3)  # a.shape = (2, 3)
    b = np.random.randn(2, 1)  # b.shape = (2, 1)
    print a
    print b
    c = a + b


    print '----------'
    print c
    print c.shape