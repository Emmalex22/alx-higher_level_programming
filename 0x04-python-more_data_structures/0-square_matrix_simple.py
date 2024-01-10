#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        neo_row = []
        for elements in row:
            neo_row.append(element ** 2)
        squared_matrix.append(neo_row)
    return squared_matrix
