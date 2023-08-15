#!/usr/bin/python3
"""

Module for task 0
0-read_file.py

"""

def read_file(filename=""):
	"""Get file and read content"""
	with open(filename, "r", encoding="UTF-8") as f:
		print(f.read(), end="")
