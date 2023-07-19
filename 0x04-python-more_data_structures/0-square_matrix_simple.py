#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	mat_x = matrix.copy()
	for a in range(len(matrix)):
		mat_x[a] = list(map(lambda x: x**2, matrix[a]))
	return (mat_x)
