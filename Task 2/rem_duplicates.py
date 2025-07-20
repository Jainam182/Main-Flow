# This program removes duplicates from a list of integers.
# Input
lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]

# Process: Remove duplicates
unique_list = []
seen = set()

for num in lst:
    if num not in seen:
        unique_list.append(num)
        seen.add(num)

# Output
print("List with duplicates removed:", unique_list)
