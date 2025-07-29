# Input
n = int(input("Enter a decimal number: "))

# Output
binary = bin(n).replace("0b", "")
print("Binary (using bin()):", binary)
