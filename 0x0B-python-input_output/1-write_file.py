#!/usr/bin/python3
"""

Module for task 1
1-write_file.py

"""

def write_file(filename="", text=""):
	"""write somw text into a file"""

	with open(filename, "w", encoding="UTF-8") as f:
		return f.write(text)
