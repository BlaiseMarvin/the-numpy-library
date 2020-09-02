#one of numpy's key features is it's n-dimensional array
#a fast and flexible container for large datasets in python

import numpy as np 

#Generate some random data
data = np.random.randn(2,3)

#Mathematical operation with the data
print(data*10)

print(data+data)
print(data.dtype)

#Creating ndarrays
#easiest way is to use the array function
#a list is a good candidate for conversion
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
print(arr1.shape)

#Nested sequences are always converted to multi dimensional arrays
data2=[[1,2,3,4,],[5,6,7,8]] # a list of lists
arr2=np.array(data2)
print(arr2)

#how many dimensions
print(arr2.ndim)

#what's the shape
print(arr2.shape)

#what's the data type
print(arr2.dtype)

#In addition to np.array, there are a number of functions for creating new arrays

#An array of zeros
zeros=np.zeros(10)
print(zeros)

#a higher dimensional zeros array
highd=np.zeros((3,6))
print(highd)

print(np.empty((2,2)))

zi=np.empty((2,3,2))
print(zi.ndim)

#arange is an array -valued version of the built in python range function
print(np.arange(15))

print(np.eye(2,3))

#Data types for the ndarrays
arr1=np.array([1,2,3],dtype=np.float64)
arr2=np.array([1,2,3],dtype=np.int32)

print(arr1.dtype)
print(arr2.dtype)

#You can explicitly convert or cast an array, from one dtype to another using the astype method
arr=np.array([1,2,3,4,5])
print(arr.dtype)

float_arr=arr.astype(np.float64)
print(float_arr)
print(float_arr.dtype)

arr=np.array([3.7,-1.2,5.8])
float_arr=arr.astype(np.int32)
print(float_arr)

#An array of strings can be converted to numeric form
numeric_strings=np.array(['1.25','9.6'],dtype=np.string_)
zx=numeric_strings.astype(np.float64)
print(zx)
