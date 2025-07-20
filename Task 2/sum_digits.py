# This program calculates the sum of the digits of a given number.
# Input
n = int(input("Enter a number: "))

# Process
digit_sum = sum(int(digit) for digit in str(n))

# Output
print("Sum of digits:", digit_sum)
