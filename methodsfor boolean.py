#Methods for Boolean arrays
import numpy as np 
arr=np.random.randn(100)
print(arr)

arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr1)
#Printing the sum of instances that are less than 3
zx=(arr1<3).sum()
print(zx)

#Two additional methods with boolean arrays, i.e. any and all
#any checks whether any one or more values in the array is true
#all checks if every value is true
bools=np.array([False,False,True,False])
print(bools.any())
print(bools.all())