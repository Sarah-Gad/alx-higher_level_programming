#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_mtrx = []
    for row in matrix:
        nw_row = list(map(lambda x: x ** 2, row))
        nw_mtrx.append(nw_row)
    return nw_mtrx
