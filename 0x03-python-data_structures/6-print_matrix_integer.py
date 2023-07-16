#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	for horizon in matrix:
		for vert in horizon:
			print("{:d}".format(vert), end=" " if vert != horizon[-1] else "")
	print()
