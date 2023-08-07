#!/usr/bin/python3
"""Class to define a rectangle"""


class Rectangle:
	"""The actual class to create a rectangle"""
	number_of_instances = 0
	print_symbol = "#"

	def __init__(self, width=0, height=0):
		""" Intialing the recangle"""
		self.width = width
		self.height = height
		Rectangle.number_of_instances += 1

	def __str__(self):
		"""Draw out the recangle into a list and 
		return"""        
		if self.__height == 0 or self.__width == 0:
			return ""
		size = str(self.print_symbol) * self.__width
		recangle = []
		for index in range(self.__height):
			recangle.append(size)
		return "\n".join(recangle)

	def __repr__(self):
		"""display our rectangle"""
		return "{:s}({:d}, {:d})".format((type(self).__name__),
										 self.__width, self.__height)

	def __del__(self):
		"""Destroy the rectangle, less one
		instance"""
		Rectangle.number_of_instances -= 1
		print("Bye rectangle...")

	@property
	def width(self):
		"""Check the width of the recangle"""
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
		"""Check the height of the recangle"""
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
		"""Return the calculated area of 
		the rectangle"""
		return self.__height * self.__width

	def perimeter(self):
		 """Return the value of the perimter of the
		recangle if height and width != 0
		else return nothing"""
		if self.__height == 0 or self.__width == 0:
			return
		return (self.__height * 2) + (self.__width * 2)

	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		"""check who big pass, return am"""
		if type(rect_1) != Rectangle:
			raise TypeError("rect_1 must be an instance of Rectangle")
		if type(rect_2) != Rectangle:
			raise TypeError("rect_2 must be an instance of Rectangle")
		if rect_1.area() >= rect_2.area():
			return rect_1
		else:
			return rect_2
	@classmethod
	def square(cls, size=0):
		"""make a square"""
		return cls(size, size)
