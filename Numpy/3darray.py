# 2D array

import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

arr3d = np.array([
    [[1,2,3],[4,5,6]],   # layer one 
    [[7,8,9],[10,11,12]] # layer two
    ])

print(arr2d)
print(arr3d[0,1,2]) # first depth , second row , third column

