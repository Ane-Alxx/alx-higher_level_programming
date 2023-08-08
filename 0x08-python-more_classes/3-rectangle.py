#!/usr/bin/python3
"""Rectangle class definition, to spawn"""


class Rectangle:
	"""
	The actual class to create a rectangle
	Attributes:
		width: rect width (integer).
		height: rect height (integer).
	"""
	def __init__(self, width=0, height=0):
		"""instancing the rectangle.

		Args:
			width: initial width of the rect(0)
			height: initial height of the rect(0)
		"""
		self.height = height
		self.width = width

	@property
	def width(self):
		"""check the current width

		Returns:
			width of the rectangle
		"""
		return self.__width

	@property
	def height(self):
		"""check the current height

		Returns:
			height of the rectangle
		"""
		return self.__height

	@width.setter
	def width(self, value):
		"""set the width of the rectangle

		Args:
			width: the value, width of the rectangle 

		Raises:
			TypeError: if value is not an integer.
			ValueError: if value is < 0.
		"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		elif value < 0:
			raise ValueError("width must be >= 0")
		else:
			self.__width = value

	@height.setter
	def height(self, value):
		"""Property setter for height of recyangle.

		Args:
			height: the value, height of the rectangle 
		Raises:
			TypeError: if value is not an integer.
			ValueError: if value is < 0.
		"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		elif value < 0:
			raise ValueError("height must be >= 0")
		else:
			self.__height = value

	def area(self):
		"""return the area of the recangle 
		height x width

		Returns:
			area
		"""
		return self.__height * self.__width

	def perimeter(self):
		"""
		calculate the perimeter of the rectangle

		Return:
		the value of the perimter of the                              
        recangle if height and width != 0                                  
        else return nothing"""
		if self.__height == 0 or self.width == 0:
			return 0
		else:
			return 2 * (self.__height + self.__width)

	def __str__(self):
		"""Draw out the recangle in the console

		Returns:
			str: the rectangle as a string of #
		"""
		rectangle = []

		if self.__width == 0 or self.__height == 0:
			return ""

		for m in range(self.__height):
			for n in range(self.__width):
				rectangle.append("#")
			rectangle.append("\n")

		rectangle.pop()

		return "".join(rectangle)
