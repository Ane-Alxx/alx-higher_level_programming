#!/usr/bin/python3
"""heres the documentation for the module"""
class Square:

"""even though we know what this is for wwe need"""
        def __init__(self, size):
		self.size = size

	@property
	def size(self):
                """this is for a new square"""
		return (self.__size)

	@size.setter
	def size(self, value):
                """this is all about getting and setting sizes"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
                """and this is for the area"""
		return (self.__size * self.__size)

	def my_print(self):
                """finally to draw the square"""
		for i in range(0, self.__size):
			[print("#", end="") for j in range(self.__size)]
			print("")
		if self.__size == 0:
			print("")
