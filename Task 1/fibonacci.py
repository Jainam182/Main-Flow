# Program to generate first n Fibonacci numbers

# Input
n = int(input("Enter how many Fibonacci numbers to generate: "))

# Process
fib_sequence = []

a, b = 0, 1
for i in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

# Output
print("Fibonacci Sequence:")
print(fib_sequence)
