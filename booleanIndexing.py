#Consider an example, where we have some data in an array and 
import numpy as np

names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
print(names.shape)

#Using the random function, to get some random, but normally distributed data
data=np.random.randn(7,4)
print(names)
print(data)


#In numpy, comparisons, such as (==) are also vectorized
#Comparison of names with Bob yields a boolean array
names=='Bob'
print(names=='Bob')

#This boolean array then, can be passed when indexing the array
z=data[names=='Bob']
print(z)

print("\n")

print(data[names=='Bob',2:])

print(names!='Bob')
print(data[names!='Bob'])

#Combining multiple boolean conditions

mask=(names=='Bob')|(names=='Will')
print(mask)
print(data[mask])

print("\n")
print(data)

#Setting values, with boolean arrays,works in a common sense way. Let's set all the negative values to zero

data[data<0]=0
print("\n")
print(data)


#Setting, whole rows, or columns using one dimensional boolean array is also easy

data[names!='Joe']=7
print(data)