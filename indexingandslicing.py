#One dimensional array indexing and slicing is similar to python lists
import numpy as np

arr=np.arange(10)
print(arr)

print(arr[5])

print(arr[5:8])

arr[5:8] = 12
print(arr)

#Unlike with python lists where slices are copies of the original array, with numpy, slices are views on the original array
arr_slice=arr[5:8]
print(arr_slice)

#Making changes in the array slice, the changes are reflected in the original array
arr_slice[1]=12345
print(arr)

#The bare slice[:], will assign to all values in an array
arr_slice[:]=64
print(arr)

#In numpy, to copy a slice, instead of a view, use the .copy() method

#Two dimensional array
#for a two dimensional array, the elements at each index, are nolonger scalers, but rather one dimensional arrays

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[2])

#So, for a two dimensional array, this is how you index

print(arr2d[0][2])

print(arr2d[0,2])

#axis 0 is the row, axis 1 is the column

#Consider the 3d array, below
arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)

print(arr3d[0].ndim)
print(arr3d[0].shape)


#Both scalar values and arrays can be assigned to arr3d[0]
old_values=arr3d[0].copy()

#Indexing with slices

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)

print(arr2d[:2]) #Slicing a 2 dimensional array like this doesn't give a scalar, it gives a one dimensional array
#remember that each index for a 2d array returns a one dimensional array
print("\n")
print(arr2d)

#we can pass multiple slices, like we did with multiple indices
print(arr2d[:2,1:])
