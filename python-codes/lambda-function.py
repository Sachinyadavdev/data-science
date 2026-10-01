square = lambda x: x * x 

print(square(8))

cube = lambda x : x * x * x

print(cube(2))

# is_even = lambda number : True if number%2 == 0 else False
is_even = lambda number : number % 2 == 0
print(is_even(572))


# Largest of Two Number 

maximum = lambda x ,y: x if x>y else y

print(maximum(45,8))

#  Celcius to Farenhit 

celcius_f = lambda c : (c * 9/5) + 32

print(celcius_f(5))

numbers = [1, 2, 3, 4, 5]

s = list(map(lambda x : x *x , numbers))
print(s)

names = ["sachin", "rahul", "amit", "priya"]

n = list(map(lambda x: x.upper(),names))
print(n)

words = ["Python", "SQL", "Pandas", "Datar466"]

print(list(map(lambda x: len(x),words)))

