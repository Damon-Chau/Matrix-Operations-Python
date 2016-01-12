def matrix_size():
    # user inputs the size of a matrix m x n (rows x columns)
    # return rows
    # return columns
    rows = input("Enter the number of rows in the matrix:")
    columns = input("Enter the number of columns" )

    return rows, columns


def matrix_input(rows, columns):
    # fill matrix with values
    # return matrix that user inputted

    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            print "Enter a number for the matrix in position ", i+1, j+1, ": "
            number = input()
            row.append(number)
        matrix.append(row)

    print "You inputted:"
    for list in matrix:
        print list

    return matrix


def matrix_addition(matrix1, matrix2):
    # add 2 matrices
    final_matrix = []

    for i in range(len(matrix1)):
        final_insidematrix = []
        for j in range(len(matrix1[i])):
            addition = matrix1[i][j] + matrix2[i][j]
            final_insidematrix.append(addition)
        final_matrix.append(final_insidematrix)

    return final_matrix


def matrix_subtraction(matrix1, matrix2):
    # subtract 2 matrices
    final_matrix = []

    for i in range(len(matrix1)):
        final_insidematrix = []
        for j in range(len(matrix1[i])):
            addition = matrix1[i][j] - matrix2[i][j]
            final_insidematrix.append(addition)
        final_matrix.append(final_insidematrix)

    return final_matrix


def matrix_transpose(rows, columns, matrix):

    transpose = []

    for i in range(columns):
        transpose_inside = []
        for j in range(rows):
            transpose_inside.append(matrix[j][i])
        transpose.append(transpose_inside)

    return transpose


def scalar_multi(matrix, constant):
    final_matrix = []
    for list in matrix:
        inside_matrix = []
        for i in range(len(list)):
            inside_matrix.append(list[i] * constant)
        final_matrix.append(inside_matrix)

    return final_matrix


def output(matrix):
    # outputs the resulting matrix
    print "The resulting matrix is: "
    for list in matrix:
        print list


def main():
    print "This application computes a number of matrix operations for 2 matrices."

    flag = True
    while flag:
        operation = raw_input("What operation do you want to perform: (add, subtract, transpose, scalar multiplication)")
        if operation == "add" or operation == "subtract" or operation == "transpose" or operation == "scalar multiplication":
            flag = False

    if operation == "add":
        rows, columns = matrix_size()
        matrix1 = matrix_input(rows, columns)
        matrix2 = matrix_input(rows, columns)

        final = matrix_addition(matrix1, matrix2)
    elif operation == "subtract":
        rows, columns = matrix_size()
        matrix1 = matrix_input(rows, columns)
        matrix2 = matrix_input(rows, columns)

        final = matrix_subtraction(matrix1, matrix2)
    elif operation == "transpose":
        rows, columns = matrix_size()
        matrix = matrix_input(rows, columns)

        final = matrix_transpose(rows, columns, matrix)
    elif operation == "scalar multiplication":
        rows, columns = matrix_size()
        matrix = matrix_input(rows, columns)
        scale = input("What number would you like to multiply matrix by? ")

        final = scalar_multi(matrix, scale)

    output(final)


main()