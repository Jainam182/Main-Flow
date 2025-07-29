# Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
matrix1 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

print("Enter elements of second matrix:")
matrix2 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

# Matrix Addition
result = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Output
print("Resultant Matrix:")
for row in result:
    print(row)
