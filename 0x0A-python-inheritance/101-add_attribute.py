#!/usr/bin/python3
"""module for add attribute function"""


def add_attribute(obj, name, value):
	"""function to add an attributr"""
	if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
		setattr(obj, name, value)
	else:
		raise TypeError("can't add new attribute")
