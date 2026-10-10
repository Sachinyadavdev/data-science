import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

mean = arr.mean()
mean2 = np.mean(arr)

print(mean)
print(mean2)

standard_d = np.std(arr)
print(f"Standard Deviation: {standard_d}")

