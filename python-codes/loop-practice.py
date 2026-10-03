numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

text = "Python"
new_text = ""
le = len(text)

for char in text:
    # print(le)
    new_text = new_text.__add__(text[le-1])
    le-=1
print(new_text)

# Nested For Loop 

for i in range(0,5):
    print("*"*5)

for i in range(0,6):
    print("*"*i)

# Nested Loop Example 
for i in range(1,6):
    for j in range (1,i+1):
        print(j,end="")
    print()

student = {
    "name": "Sachin",
    "age": 27,
    "city": "Delhi"
}

for key, value in student.items():  # Unpacking the Values 
    print(f"{key}:{value}")

