# This program calculates the length of a given string without using built-in functions.
# Input
text = input("Enter a string: ")

# Process: Calculate the length of the string
count = 0
for char in text:
    count += 1

# Output
print("Length of the string:", count)
