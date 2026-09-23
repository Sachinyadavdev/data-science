# Clean User Input 

name = "   Sachin Yadav   "

print(name)
print(name.strip())

text = "I am learning Java"

print(text.replace('Java','Python'))

sentence = "Python Java SQL React HTML"

print(sentence.split())

words = ["Python","is","easy","to","learn"]

words_join = " ".join(words)

print(words_join)

# Check the Content 

email = "sachinyadav@gmail.com"

# if email.endswith('@gmail.com') and email.startswith('sachinyadav') and email.__contains__('@'):
#     print("Valid Email")

# else:
#     print("Invalid Email Entered")

print('@' in email)
print(email.endswith('.com'))
print(email.startswith('sachin'))
print('gmail' in email)

# Count the Vowels in the String

sentence2 = "Data Science is Interesting"
a = 0 
e = 0
i = 0
o = 0
u = 0
# print(a)
for vo in sentence2.lower():

 if vo == 'a':
       
       a+=1
 elif vo == 'e':
       
       e+=1
 elif vo == 'i':
       
       i+=1
 elif vo == 'o':
       
       o+=1
 elif vo == 'u':
       
       u+=1

print(f"a :{a}")
print(f"e :{e}")
print(f"i :{i}")
print(f"o :{o}")
print(f"u :{u}")
    