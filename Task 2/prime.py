# This program checks if a number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check for factors from 3 to sqrt(n)
    for i in range(3, (n // 2) + 1, 2):
        if n % i == 0:
            return False
    return True

# Input
num = int(input("Enter a number: "))

# Output
print("Prime Number:", is_prime(num))
