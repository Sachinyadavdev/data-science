text = "programming"

frequency ={}
for char in text:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char] = 1

print(frequency.keys())

unique_char = ""
for u_char in frequency:
    unique_char+=u_char

print(unique_char)