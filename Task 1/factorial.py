# Program to compute factorial of a number

# Input
n = int(input("Enter a number: "))

# Process
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Output
print("Factorial is:", factorial)
