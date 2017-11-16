import numpy as np

A = np.random.randn(4,3)
print A

B = np.sum(A, axis = 1, keepdims = True)
print B.shape

B = np.sum(A, axis = 1, keepdims = False)
print B.shape


hidden_layer_sizes = [1, 2, 3, 4, 5, 20, 50]
for i, n_h in enumerate(hidden_layer_sizes):
    print i, n_h