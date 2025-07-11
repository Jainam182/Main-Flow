# Program to check if a number is an Armstrong number

# Input
num = int(input("Enter a number: "))

# Process
digits = str(num)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)

# Output
print("Armstrong Number:", total == num)
