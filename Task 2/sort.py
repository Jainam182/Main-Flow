# This program sorts a list of integers using the Bubble Sort algorithm.
# Input
lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]

# Process: Bubble Sort Algorithm
n = len(lst)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            # Swap
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Output
print("Sorted List:", lst)
