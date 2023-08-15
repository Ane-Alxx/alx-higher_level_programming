#!/usr/bin/python3
"""

Module for task 5
5-save_to_json_file.py

"""

def save_to_json_file(my_obj, filename):
	"""write an obj to txt file
	args:
		my_obj: the object
		filename: the file
	returns:
		my_obj in file
	"""

	with open(filename, "w", encoding="UTF-8") as f:
		return json.dump(my_obj, f)
