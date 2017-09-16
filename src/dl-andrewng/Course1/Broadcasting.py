import numpy as np

# https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html

a = np.array([10,20,30])
b = np.array([10])

print a/b

a = np.array([[10,20,30],[40,50,60]])
print a
print np.sum(a, axis=0)
print np.sum(a, axis=1)

a = np.random.randn(5,1)
print a.T
print np.dot(a,a.T)