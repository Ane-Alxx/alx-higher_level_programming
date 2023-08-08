#!/usr/bin/python3

def safe_print_division(a, b):
	"""function to divide two integers
	and display the results"""

	answer = 0

	try:
		answer = a/b
	except(TypeError,ZeroDivisionError):
		answer = None
	finally:
		print("Inside result: {}".format(answer))
	return answer