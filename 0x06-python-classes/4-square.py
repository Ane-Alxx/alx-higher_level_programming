#!/usr/bin/python3
"""this is the solution for task 4"""

class Square:
	"""a class Square that defines a square by:
	based on task 3 """
		self.size = size

	@property
	def size(self):
                """This is for the size"""
		return (self.__size)

	@size.setter
	def size(self, value):
                """"this is for the size"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
                """this is for the area"""
		return (self.__size * self.__size)
