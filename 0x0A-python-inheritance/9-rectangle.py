#!/usr/bin/python3

"""
Module for method for class objects
for a trail of inheritance, instancing and
object spawning.

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
	"""A class for base geometry for a rectangle"""

	def __init__(self, width, height):
		"""method for self, width, height"""
		
		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height

	def area(self):
		"""method for class area"""

		return self.__width * self.__height

	def __str__(self):
		"""__str__ method magic string string"""

		return "[Rectangle] {}/{}".format(self.__width, self.__height)
