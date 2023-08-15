#!/usr/bin/python3
"""

Module for task 100
100-append_after.py

"""

def append_after(filename="", search_string="", new_string=""):
	"""some random information
	that is supposed to be the documentations"""

	tt = ""
	with open(filename) as r:
		for d in r:
			tt += d
			if search_string in d:
				tt += new_string
	with open(filename, "w") as w:
		w.write(tt)
