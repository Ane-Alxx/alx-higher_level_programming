#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

	"""function to print list of items
	on a single line followed by
	a new line"""

	tracker = 0

	for b in range(x):
		try:
			print("{}".format(my_list[b]), end="")
			tracker += 1
		except IndexError:
			break
	print()

	return (tracker)
