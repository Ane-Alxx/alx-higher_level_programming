#!/usr/bin/python3
"""Class to define a rectangle"""

class Rectangle:
	"""The actual class to create a rectangle"""

	def __init__(self, width=0, height=0):
		""" Intialing the recangle"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""Check the width of the rectngl"""
		return self.__width

	@width.setter
	def width(self, value):
		"""Set the value of the recangle width"""
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""check the height of the rectangle"""
		return self.__height

	@height.setter
	def height(self, value):
		"""set the value of the recangle height"""
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value
