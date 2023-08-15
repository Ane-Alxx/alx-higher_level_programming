#!/usr/bin/python3
"""

Module for task 6
6-load_from_json_file.py

"""
import json

def load_from_json_file(filename):
	"""load from file
	args:
		filename: the file
	returns:
		f
	"""

	with open(filename, "r", encoding="UTF-8") as f:
		return json.load(f)
