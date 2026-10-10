import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

result = []

for num in arr:
    result.append(num**2)

print(result)

new_result = arr ** 2

print(new_result)