#!/usr/bin/python3
"""this is the solutio for task two"""

class Square:
	""" a class Square that defines a square by:
	working from prev task"""

	def __init__(self, size=0):
                """this is for the squaer"""

		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size

	def area(self):
                """this is to return the area"""
		return (self.__size * self.__size)
