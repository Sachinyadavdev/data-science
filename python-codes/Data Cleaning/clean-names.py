cities = [
    " Delhi",
    "delhi ",
    "DELHI",
    " Mumbai",
    "MUMBAI",
    " Chennai "
]

for i in range(len(cities)):
    cities[i] = cities[i].strip().lower().title()

print(cities)

names = [
    " sachin yadav ",
    "RAHUL SHARMA",
    " priya singh",
    "AMIT kumar "
]

for i in range(len(names)):
    names[i] = names[i].strip().lower().title()
    print(names[i])

