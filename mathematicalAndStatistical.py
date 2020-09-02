#A set of mathematical functions 
#Computing some aggregated statistics on some randomly generated data
import numpy as np 
arr=np.random.randn(5,4)
print(arr)

#Computing the mean
print(arr.mean(axis=0))

#or 
print(np.mean(arr))

#Summing everything up
print(arr.sum())

#Mean and sum take axis arguments
#axis=1, means take the mean across the columns
#axis=0, means take the mean across the rows

arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr1)

print(arr1.std())
print(arr1.argmax(axis=1))

print(np.argwhere(arr1==5))


#Methods for Boolean Arrays