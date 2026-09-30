text = input("Enter the text: ")

# remove the spaces and dots from the text

text = text.lower()
text = text.strip()

length = text.__len__()
palindrome = ""

for char in text:
    # print(text[length-1])
    palindrome = palindrome.__add__(text[length-1])
    length-=1

print(palindrome)

if palindrome == text:
    print("The Given text is Palindrome")
else:
    print("It is Not Palindrome!")