#Fancy indexing-describe indexing, using integer arrays
#Suppose, we had an 8*4 array

import numpy as np 

arr=np.empty((8,4))

for i in range(8):
    arr[i]=i

print(arr)

#To select particular rows, in particular order
#To select a subset of rows in particular order,simply pass a list or ndarray of integers specifying a particular order

print(arr[[4,3,0,6]])

#Still on fancy indexing
print(arr[[-3,-5,-7]])

#Passing multi-dimensional index arrays
arr = np.arange(32).reshape((8,4))
print(arr)

print(arr[[1,5,7,2],[0,3,1,2]])