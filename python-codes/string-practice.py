name = "Alice6"


# para = """This is the paragraph name 
# as the python interpreter and the anme of this is known as the is best python game"""

# print(para)
# name[1] = "T" string are immutable and can not be changed.
# print(name[0])

# print(name.lower())
# name.lower()
# print(name)

# print(para.strip()) 

# print(para.replace("This", "Mai hu na")) 
# print(para.split()) # It will make the split the string into the list

# list_name = ['This', 'is','name']

# print(name.join(list_name))


# print(para.find('is')) # Find the Occurence of the string 
# print(para.count('this')) # This function will find the number of occurence and it is case sensitive 

# print(para.startswith('This')) # This will return the value of True and False if it retuen the correct and false statement.

# print(para.isdigit())
# print(name.isalpha())

# print(name.isalnum())

text = "Data Science is the New Career"

# Lenght of the String 

print(len(text))
print(text.__len__())
print(text[-1])
print(text[5])

# Reverse the String 

print(text[::-1])

# Find the Number of Characters 

count = len(text.replace(" ","")) # It will replace the white space from the string

print(count)

# Using Loops 

count = 0

for char in text:
    if char != " ":
     count += 1

print(count)

# Find the Number of Spaces in the String
count_sp = 0
for space in text:
   if space == " ":
     count_sp +=1

print(count_sp)


    