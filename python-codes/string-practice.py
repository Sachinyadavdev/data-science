name = "Alice6"


para = """This is the paragraph name 
as the python interpreter and the anme of this is known as the is best python game"""

print(para)
# name[1] = "T" string are immutable and can not be changed.
# print(name[0])

# print(name.lower())
# name.lower()
# print(name)

print(para.strip()) 

# print(para.replace("This", "Mai hu na")) 
print(para.split()) # It will make the split the string into the list

list_name = ['This', 'is','name']

print(name.join(list_name))


print(para.find('is')) # Find the Occurence of the string 
print(para.count('this')) # This function will find the number of occurence and it is case sensitive 

print(para.startswith('This')) # This will return the value of True and False if it retuen the correct and false statement.

print(para.isdigit())
print(name.isalpha())

print(name.isalnum())
