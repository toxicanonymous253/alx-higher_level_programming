#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    duplicat_matrix = []
    for row in matrix:
        duplicat_row = []
        for element in row:
            duplicat_row.append(element ** 2)
        duplicat_matrix.append(duplicat_row)
    return duplicat_matrix
