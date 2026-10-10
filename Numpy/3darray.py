# 2D array

import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

arr3d = np.array([
    [[1,2,3],[4,5,6]],   # layer one 
    [[7,8,9],[10,11,12]] # layer two
    ])

print(arr2d)
print(arr3d[0,1,2]) # first depth , second row , third column

print(arr3d[:,0,1])
print(arr3d[:,0,:])
print(arr3d[:,0,1:3])

arr = np.array([
    [1,2,3],
    [4,5,6]
])

arr[:,1] = 0

print(arr)

# Checking the Datatype of the array 
print(arr.dtype)

new_int = arr.astype(np.int32)

print(new_int.dtype)  # This is how you can change the data type 

