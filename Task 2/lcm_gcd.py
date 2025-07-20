# This program calculates the GCD and LCM of two integers.
# Euclidean algorithm
def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Ensure GCD is positive

# Calulating LCM using GCD
def compute_lcm(a, b):
    gcd = compute_gcd(a, b)
    return abs(a * b) // gcd if gcd != 0 else 0

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Process: Calculate GCD and LCM
gcd = compute_gcd(a, b)
lcm = compute_lcm(a, b)

print("GCD:", gcd)
print("LCM:", lcm)
