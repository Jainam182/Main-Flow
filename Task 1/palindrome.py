# Program to check if a string is a palindrome

# Input
text = input("Enter a string: ")

# Process
is_palindrome = text == text[::-1]

# Output
print("Palindrome:", is_palindrome)
