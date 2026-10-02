numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda x: x%2==0, numbers)))
print(list(filter(lambda x: x%2==0, numbers)))

numbers2= [10, 55, 23, 89, 45, 100]

print(list(filter(lambda x : x>50, numbers2)))

names = [
    "Amit",
    "Rahul",
    "Ankit",
    "Priya",
    "Ananya"
]

print(list(filter(lambda x: x[0].lower()=='a',names)))

