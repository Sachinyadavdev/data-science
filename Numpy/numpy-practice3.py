# create the numpy array with the values from 20 to 100 and print its shape 

import numpy as np

arr = np.arange(20, 101,10)

print(arr)
print(arr.shape) 

arr2 = np.array([23,4,56,7,8,9])

print(arr2[4])
print(arr2[-1]) # This will print the last array element of the array

print(arr2[1:3]) 
print(arr2[:2])
print(arr2[::2]) # This will print every second element of the Number

  # fancy Indexing 

idx = [2,4,5]

print(arr2[idx])

# Boolean Masking 

filt = arr2 > 20

print(arr2[filt])

# create a 3 x 3 array filled with random numbers and print its shape

new_arr = np.arange(1,9)
new_arr2 = np.ones(9)
new_arr3 = np.full(3,4)
new_arr4 = np.array([
    [1,2,3],
    [2,5,6],
    [2,5,6]
])

print(new_arr)
print(new_arr2)
print(new_arr3)
print(new_arr4)
print(new_arr.shape)

new_arr5 = np.random.rand(3,3) # Here it has created the random 3 x 3 matrix 

print(new_arr5) 
print(new_arr5.shape) 

int_arr = new_arr5.astype(int)
print(int_arr)

numbers = np.array([1,2,3,4,5,6])
ind = [1,3,5]
print(numbers[ind])

