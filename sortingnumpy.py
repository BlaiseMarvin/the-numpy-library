#Numpy's arrays can also be sorted 
import numpy as np 
arr=np.random.randn(6)
print(arr)

arr.sort()
print(arr)

#In a multi-dimensional array, you can sort each one dimensioanl section of values by passing an axis number to sort

arr=np.random.randn(5,3)
print("\n")
print(arr)

print("\n")
arr.sort(1)
print(arr)

#sort with arg 1, returns all rows sorted

arr2=np.array([[4,3,2,1],[8,7,6,5],[12,11,10,9]])
print(arr2)
arr2.sort(0)
print(arr2)

#Top level sorting
arr3=np.array([[4,3,2,1],[8,7,6,5],[12,11,10,9]])
print("\n")
print(np.sort(arr3,axis=1))