import numpy as np

# 2D Array

arr = np.array([
    [1,2,3],
    [3,4,7],
    [9,6,8]
])

print(arr)
print(arr[0,1:3])

print(np.sum(arr,axis=0))  # Summing along the rows 
print(np.sum(arr,axis=1))  # Summing along the Columns

# Slicing to exatrct the part of the Array

print(arr[0:2,1:3])