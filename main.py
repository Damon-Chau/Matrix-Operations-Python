def matrix_size():
    # user inputs the size of a matrix m x n (rows x columns)
    # return rows
    # return columns
    rows = input("Enter the number of rows in the matrix:")
    columns = input("Enter the number of columns" )

    return rows, columns


def matrix_input(rows, columns):
    # fill matrix with values

    matrix = []

    for i in range (rows):
        row = []
        for j in range(columns):
            print "Enter a number for the matrix in position ", i, " ", j, ":"
            number = input()
            row.append(number)
        matrix.append(row)

    return matrix

def matrix_addition(matrix1, matrix2):
    # add 2 matrices
    final_matrix = []
    if len(matrix1) == len(matrix2):
        for i in range (len(matrix1)):
            if len(matrix1[i]) != len(matrix2[i]):
                return "The size of the matrices are not the same. Please re-enter the matrix."
    else:
        return "The size of the matrices are not the same. Please re-enter the matrix."

    for i in range(matrix1):
        final_insidematrix = []
        for j in range (matrix1[i]):
            addition = matrix1[i][j] + matrix2[i][j]
            final_insidematrix.append(addition)
        final_matrix.append(final_insidematrix)

    return final_matrix


def matrix_subtraction(matrix1, matrix2):
    # subtract 2 matrices
    final_matrix = []
    if len(matrix1) == len(matrix2):
        for i in range (len(matrix1)):
            if len(matrix1[i]) != len(matrix2[i]):
                return "The size of the matrices are not the same. Please re-enter the matrix."
    else:
        return "The size of the matrices are not the same. Please re-enter the matrix."

    for i in range(matrix1):
        final_insidematrix = []
        for j in range (matrix1[i]):
            addition = matrix1[i][j] - matrix2[i][j]
            final_insidematrix.append(addition)
        final_matrix.append(final_insidematrix)

    return final_matrix


def output():
    a = 0 # temporary placeholder for function content


def main():
    print "This application computes a number of matrix operations for 2 matrices."


main()