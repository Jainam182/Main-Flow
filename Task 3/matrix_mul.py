# Input dimensions
rows_A = int(input("Enter rows for Matrix A: "))
cols_A = int(input("Enter columns for Matrix A: "))
rows_B = int(input("Enter rows for Matrix B: "))
cols_B = int(input("Enter columns for Matrix B: "))

# Check multiplication condition
if cols_A != rows_B:
    print("Matrix multiplication not possible! (Columns of A must equal rows of B)")
else:
    # Input Matrix A
    print("Enter elements of Matrix A:")
    A = [[int(input(f"A[{i+1}][{j+1}]: ")) for j in range(cols_A)] for i in range(rows_A)]

    # Input Matrix B
    print("Enter elements of Matrix B:")
    B = [[int(input(f"B[{i+1}][{j+1}]: ")) for j in range(cols_B)] for i in range(rows_B)]

    # Initialize Result Matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Matrix Multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    # Output
    print("Resultant Matrix:")
    for row in result:
        print(row)
