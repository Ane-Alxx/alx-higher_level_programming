#!/usr/bin/python3
"""Function to print a square"""
def print_square(size):
	""" function prints square with '#' 
	if:
		argument for size is an integer"""
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")
	for index in range(size):
		print("#" * size)
