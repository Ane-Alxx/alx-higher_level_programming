#!/usr/bin/python3
"""Class to define a rectangle"""


class Rectangle:
	"""The actual class to create a rectangle"""

	def __init__(self, width=0, height=0):
		""" Intialing the recangle"""
		self.width = width
		self.height = height

	def __str__(self):
		"""Draw out the recangle in the console"""
		if self.__height == 0 or self.__width == 0:
			return ""
		size = "#" * self.__width
		recangle = []
		for index in range(self.__height):
			recangle.append(size)
		return "\n".join(recangle)

	def __repr__(self):
		"""display our rectangle"""
		return "{}({}, {})".format((type(self).__name__), self.__width,
								   self.__height)

	@property
	def width(self):
		"""Check the width of the rectngl"""
		return self.__width

	@width.setter
	def width(self, value):
		"""set the value of the recangle width"""
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""Check the height of the rectngl"""
		return self.__height

	@height.setter
	def height(self, value):
		"""set the value of the recangle height"""
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

	def area(self):
		"""return the value of the recangle area"""
		return self.__height * self.__width

	def perimeter(self):
		"""Return the value of the perimter of the
		recangle if height and width != 0
		else return nothing"""
		if self.__height == 0 or self.__width == 0:
			return
		return (self.__height * 2) + (self.__width * 2)
