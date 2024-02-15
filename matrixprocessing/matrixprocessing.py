"""Matrix Processing"""

# define a function to read a matrix from user input
def read_matrix():
    # get the number of rows and columns from the user
    rows, cols = map(int, input("Enter matrix size: > ").split())
    matrix = []
    print("Enter matrix:")
    # populate the matrix by reading rows from the user
    for _ in range(rows):
        row = list(map(float, input("> ").split()))
        matrix.append(row)
    return matrix, rows, cols


# define a function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# define a function to add two matrices
def add_matrices():
    print("Enter size of first matrix:")
    matrix_a, rows_a, cols_a = read_matrix()

    print("Enter size of second matrix:")
    matrix_b, rows_b, cols_b = read_matrix()

    # check if matrices have the same dimensions
    if rows_a != rows_b or cols_a != cols_b:
        print("ERROR")
    else:
        # add corresponding elements of the matrices
        result = [[0 for _ in range(cols_a)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_a):
                result[i][j] = matrix_a[i][j] + matrix_b[i][j]

        print("The result is:")
        print_matrix(result)


# define a function to multiply a matrix by a constant
def multiply_by_constant():
    matrix, rows, cols = read_matrix()
    constant = float(input("Enter constant: > "))

    # multiply each element of the matrix by the constant
    result = [[constant * matrix[i][j] for j in range(cols)] for i in range(rows)]
    print("The result is:")
    print_matrix(result)


# define a function to multiply two matrices
def multiply_matrices():
    print("Enter size of first matrix:")
    matrix_a, rows_a, cols_a = read_matrix()
    print("Enter size of second matrix:")
    matrix_b, rows_b, cols_b = read_matrix()

    # check if matrices can be multiplied
    if cols_a != rows_b:
        print("ERROR")
    else:
        # multiply matrices using nested loops
        result = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in
                  range(rows_a)]
        print("The result is:")
        print_matrix(result)


# define a function to transpose a matrix
def transpose_matrix():
    matrix, rows, cols = read_matrix()
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    choice = int(input("Your choice: > "))

    # transpose the matrix based on user's choice
    if choice == 1:
        result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    elif choice == 2:
        result = [[matrix[cols - 1 - j][rows - 1 - i] for j in range(cols)] for i in range(rows)]
    elif choice == 3:
        result = [row[::-1] for row in matrix]
    elif choice == 4:
        result = matrix[::-1]
    else:
        print("Invalid choice.")
        return

    print("The result is:")
    print_matrix(result)


# define a function to calculate the determinant of a matrix
def calculate_determinant(matrix):
    size = len(matrix)

    # base cases for 1x1 and 2x2 matrices
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        # recursive case for larger matrices
        det = 0
        for i in range(size):
            submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
            det += matrix[0][i] * calculate_determinant(submatrix) * (-1) ** i
        return det


# define a function to find the inverse of a matrix
def inverse_matrix():
    matrix, rows, cols = read_matrix()

    # calculate the determinant of the matrix
    det = calculate_determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    # calculate the cofactor matrix, adjugate matrix, and inverse matrix
    cofactor_matrix = [
        [((-1) ** (i + j)) * calculate_determinant([row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]) for
         j in range(cols)] for i in range(rows)]
    adjugate_matrix = [[cofactor_matrix[j][i] for j in range(rows)] for i in range(cols)]
    inverse = [[adjugate_matrix[i][j] / det for j in range(cols)] for i in range(rows)]

    print("The result is:")
    print_matrix(inverse)


# main loop to interact with the user
while True:
    print(
        "\n1. Add matrices\n2. Multiply matrix by a constant"
        "\n3. Multiply matrices\n4. Transpose matrix"
        "\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    # user's choice
    choice = int(input("Your choice: > "))

    if choice == 1:
        add_matrices()
    elif choice == 2:
        multiply_by_constant()
    elif choice == 3:
        multiply_matrices()
    elif choice == 4:
        transpose_matrix()
    elif choice == 5:
        matrix, _, _ = read_matrix()
        det = calculate_determinant(matrix)
        print("The result is:")
        print(det)
    elif choice == 6:
        inverse_matrix()
    elif choice == 0:
        break
    else:
        print("Invalid choice.")
