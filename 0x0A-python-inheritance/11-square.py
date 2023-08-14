#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""
Module for method for class objects
for a trail of inheritance, instancing and
object spawning.

"""


class Square(Rectangle):
	"""A class for base geometry for a square"""

	def __init__(self, size):
		"""method for class area"""

		super().__init__(size, size)
		self.integer_validator("size", size)
		self.__size = size

	def area(self):
		"""method for class area"""

		return self.__size ** 2

	def __str__(self):
		return "[Square] {}/{}".format(self.__size, self.__size)
