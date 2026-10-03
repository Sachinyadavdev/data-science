import numpy as np 

l1 = np.array([2,4,6,7,9,3])

print(l1)
print(l1.shape)
print(l1.ndim)
print(l1.size)
print(l1.dtype)

numbers = np.array([10, 20, 30, 40, 50])

# find the sum of the numbers from the array in the np

sum_numbers  = np.sum(numbers)

print(sum_numbers)

# Mean

mean_numbers = np.mean(numbers)

print(mean_numbers)

# Maximum 

print(np.max(numbers))

# Minimum 

print(np.min(numbers))

# Standard Deviation 

print(np.std(numbers))

numbers = np.array([10, 25, 30, 45, 50, 65, 70])

greaten_40 = numbers[numbers > 40]
greater_30_60 = numbers[(numbers >= 30) & (numbers <= 60)]

print(greater_30_60)