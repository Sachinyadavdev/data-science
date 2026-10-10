import numpy as np

arr = np.array([1,2,2,3,4,5,6,7,8,9])

mean = arr.mean()
mean2 = np.mean(arr)

print(mean)
print(mean2)

standard_d = np.std(arr)
print(f"Standard Deviation: {standard_d}")

variation = np.var(arr)
print(f"Variation: {variation}")

minimum = np.min(arr)
print(f"Minimum: {minimum}")

maximum = np.max(arr)
print(f"Maximum: {maximum}")

sumof = np.sum(arr)
print(f"Sum of: {sumof}")

percentile2 = np.percentile(arr,100)
print(f"Percentile: {percentile2}")

indexofmin = np.argmin(arr)
print(f"Index of Min: {indexofmin}")

unique = np.unique(arr)
print(f"Unique Element of: {unique}")

differenceof = np.diff(arr)
print(f"Difference of Nth: {differenceof}")

logerr = np.log(arr)
print(f"The Log of the Array: {logerr}")