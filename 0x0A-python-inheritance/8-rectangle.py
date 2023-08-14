#!/usr/bin/python3

"""
Module for method for class objects
for a trail of inheritance, instancing and
object spawning.

"""

class Rectangle(BaseGeometry):
	"""A class for base geometry for a rectangle"""

	def __init__(self, width, height):
		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height
