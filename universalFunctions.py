#A universal function, or a ufunc is a function that performs element wise operations on data in ndarrays.
#Think of them as fast vectorized wrappers, that can take on one  or more scalar values, to produce one or more scalar results

import numpy as np 

arr=np.arange(10)
print(arr)

#Square root
print(np.sqrt(arr))

#exponential
print(np.exp(arr))

#Binary ufuncs, take two arrays
x=np.random.randn(8)
y=np.random.randn(8)

print(x)
print(y)

#Maximum, compares, each of two items in both arrays and produces the maximum
print(np.maximum(x,y))