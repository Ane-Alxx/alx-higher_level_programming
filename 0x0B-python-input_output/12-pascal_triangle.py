#!/usr/bin/python3
"""
Module for task 12
12-pascal_triangle.py
"""

def pascal_triangle(n):
	"""returns a pascal triangle
	in form of lists"""

	if n <= 0:
		return ""

	p_triangle = [[1]]
	while len(p_triangle) != n:
		pt = p_triangle[-1]
		cont = [1]
		for m in range(len(pt) - 1):
			cont.append(pt[m] + pt[m + 1])
		cont.append(1)
		p_triangle.append(cont)

	return p_triangle
