import numpy as np 
arr=np.arange(15).reshape((3,5))
print(arr)

#Transposing
print(arr.T)

#The dot product
#np.dot(arr.T,arr) the dot product between the transpose of arr, and arr

arr=np.random.randn(6,3)
print(arr)
