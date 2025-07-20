# This program reverses a list of integers in place.
# Input
lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]

# Process: Reverse the list in place
start = 0
end = len(lst) - 1

while start < end:
    # Swap elements at start and end
    lst[start], lst[end] = lst[end], lst[start]
    start += 1
    end -= 1

# Output
print("Reversed List:", lst)
