import numpy as np 
#with numpy arrays, we have vectorization, i.e. batch operations on the data inside the ndarray without havin to write for loops

arr=np.array([[1,2,3],[4,5,6]],dtype=np.float64)
print(arr)

print(arr*arr) # it multiplies each element, with the corresponding element in the other array
print(arr-arr)

#Arithmetic operations with scalars, propagate the scalar argument to each element in the array

print(1/arr)

print(arr*0.5)

#Comparisons between arrays of the same size yields boolean arrays

arr2=np.array([[0,4,1],[7,2,12]],dtype=np.float64)

print(arr2)

#comparisons yield boolean arays of the same size
print(arr>arr2)


