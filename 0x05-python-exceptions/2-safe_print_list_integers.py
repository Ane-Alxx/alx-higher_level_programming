#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
	"""function to print the no of 
	integers in a list"""

	tracker = 0
	for b in range(0, x):
		try:
			print("{:d}".format(my_list[b]), end="")
			tracker += 1
		except (ValueError, TypeError):
			continue
	print()

	return tracker
