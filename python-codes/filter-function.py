numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda x: x%2==0, numbers)))
print(list(filter(lambda x: x%2==0, numbers)))