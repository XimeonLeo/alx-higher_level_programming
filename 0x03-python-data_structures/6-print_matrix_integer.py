#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for elem in range(len(matrix[row])):
            if elem != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][elem]), end='')
        print()
