#!/usr/bin/python3
"""this is the docummentation comment"""

class Square:
	"""a class Square that defines a square by:
	working from prev task"""

	def __init__(self, size=0):
                """This is all for the square"""

		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size
