#Numpy has some basic set operations for one-dimensional ndarrays,
#Commonly used one is np.unique, which returns the sorted unique values in an array

import numpy as np 
names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])

#unique returns sorted unique values
print(np.unique(names))

ints=np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(ints)
print(np.unique(ints))

#Another function: np.in1d,tests the membership of values in one array, in another returning boolean array

values=np.array([6,0,0,3,2,5,6])
print(np.in1d(values,[2,3,6]))
