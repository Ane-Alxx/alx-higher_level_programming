#!/usr/bin/python3

def safe_print_integer(value):

	"""function to print an integer value
	if integer rewturn true else
	return false
	"""
	try:
		print("{:d}".format(value))
		return True
	except (TypeError, ValueError):
		return False
