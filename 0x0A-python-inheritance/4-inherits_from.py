#!/usr/bin/python3

"""
Module for method for class objects
for a trail of inheritance, instancing and
object spawning.

"""
def inherits_from(obj, a_class):
	"""Class method for inheris from"""
	
	return False if type(obj) is a_class else isinstance(obj, a_class)
