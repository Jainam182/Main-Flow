# This program counts the number of vowels and consonants in a given string.
# Input
text = input("Enter a string: ")

# Initialize counters
vowel_count = 0
consonant_count = 0

# Set of vowels
vowels = set('aeiouAEIOU')

# Process
for char in text:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Output
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
