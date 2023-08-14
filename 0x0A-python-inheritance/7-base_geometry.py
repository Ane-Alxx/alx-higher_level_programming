#!/usr/bin/python3

"""
Module for method for class objects
for a trail of inheritance, instancing and
object spawning.

"""


class BaseGeometry:
	"""A class for base geometry"""


	def area(self):
		"""area method creator"""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""integer validator method"""

		if type(value) is not int:
			raise TypeError("{} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name))
