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
