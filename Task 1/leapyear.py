# Program to check for a leap year

# Input
year = int(input("Enter a year: "))

# Process
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Output
print("Leap Year:", is_leap)
