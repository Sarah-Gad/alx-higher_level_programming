#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    thelen = len(matrix)
    i = 0
    while i < thelen:
        j = 0
        while j < len(matrix[i]):
            print("{:d} " .format(matrix[i][j]), end="")
            j += 1
        print()
        i += 1
