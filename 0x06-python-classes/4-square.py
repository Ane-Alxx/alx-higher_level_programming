#!/usr/bin/python3


class Square:
	"""a class Square that defines a square by:
	based on task 3 """
		self.size = size

	@property
	def size(self):
		return (self.__size)

	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		return (self.__size * self.__size)
