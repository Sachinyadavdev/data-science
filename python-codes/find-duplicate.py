text = "Programmiiiiiingaaaall"

frequency = {}


# Step 1, find the Frequency of the letters
for char in text:
  
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

print(frequency)


for char, count in frequency.items():
    if count > 1:
        print(f"{char}:{count}")