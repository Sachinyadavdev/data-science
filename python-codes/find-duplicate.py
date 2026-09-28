text = "Programmiiiiiingaaaa"

new_text = set()
count = 0
frequency = {}
for letter in text:
    count+=1
    new_text = new_text.union(set(letter))
    if letter in frequency:
        frequency[letter] +=1
    else:
        frequency[letter] = 1

print(count)
print(new_text)
print(frequency)