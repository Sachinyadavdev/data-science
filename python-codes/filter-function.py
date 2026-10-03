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

words = [
    "Python",
    "SQL",
    "Pandas",
    "AI",
    "Machine",
    "Data"
]

print(list(filter(lambda x: len(x) > 5, words)))

# lambda + Sorting - list in the tuple 

students = [
    ("Sachin", 85),
    ("Rahul", 72),
    ("Priya", 92),
    ("Amit", 65)
]

sorted_names = sorted(students,key=lambda student: student[1], reverse=True)

print(sorted_names)

# Reduce Function

from functools import reduce

numbers = [1, 2, 3, 4, 5]

print(reduce(lambda x,y: x+y,numbers))

