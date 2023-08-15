#!/usr/bin/python3
"""

Module for task 4
4-from_json_string.py

"""

def from_json_string(my_str):
	"""return the json string rep of str
	args:
		my_str: the string
	returns:
		my_str
	"""

	return json.loads(my_str)
