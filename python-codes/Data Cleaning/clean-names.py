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