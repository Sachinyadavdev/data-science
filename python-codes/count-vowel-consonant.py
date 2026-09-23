# Count Vowel and Constonants
text = "Salary talks are tricky. Let the Worklife pros in the Glassdoor community be your guide to a paycheck you can feel great about."

# Filter the text and remove the spaces and dots from the text
new_text = text.replace(" ","")
new_text2 = new_text.replace(".","")
final_text = new_text2.lower()

# Logic to Find the count of Vowels and Consonant

vowels = 0
consonants = 0
unique_vowels = set()
unique_consonants = set()

frequency = {}

for letter in final_text:
    # Frequency of Vowels and Consonants
    if letter in frequency:
        frequency[letter] +=1
    else:
        frequency[letter] = 1

    if letter == 'a' or letter == 'e' or letter =='i' or letter =='o' or letter =='u':
        vowels+=1
        unique_vowels.add(letter)
    else:
        consonants+=1
        unique_consonants.add(letter)

    # Find Unique Vowels and Consonant 

print(f"Number of Vowels: {vowels}")
print(f"Number of Consonants: {consonants}")
print(f"Unique Vowels: {unique_vowels}")
print(f"Unique Consonants: {unique_consonants}")
print(f"The Frequency of the Letters: {frequency} ")



