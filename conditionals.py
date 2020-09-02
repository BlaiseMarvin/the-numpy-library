#Using np.where
import numpy as np 
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])

cond=np.array([True,False,True,True,False])

#want to iterate over the conditional, when true, print xarr,when false, print yarr
result=np.where(cond,xarr,yarr)
print(result)

#Use of this np.where is in matrix formation and generation

arr = np.random.randn(4,4)
print(arr)

arr=arr>0
print(arr)

zx=np.where(arr,2,-2)
print(zx)

#Using np.where, we can combine scalars and arrays
arr=np.random.randn(4,4)
print(arr)

arr=np.where(arr>0,2,arr)
print(arr)
