#!/usr/bin/python3
"""

Module for task 2
2-append_write.py

"""

def append_write(filename="", text=""):
	"""append some string to our text file
	args:
		filename: the name of the file
		text: what we be appending
	returns:
		text
		"""
	with open(filename, "a", encoding="UTF-8") as f:
		return f.write(text)
