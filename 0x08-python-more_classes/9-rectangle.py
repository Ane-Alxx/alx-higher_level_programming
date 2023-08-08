#!/usr/bin/python3
"""Rectangle class definition, to spawn"""


class Rectangle:
	"""
	Class that defines properties of rectangle by: (based on 6-rectangle.py).

	Attributes:
		width (int): width of the rectangle.
		height (int): height of the rectangle.
	"""

	number_of_instances = 0
	print_symbol = "#"

	def __init__(self, width=0, height=0):
		"""
		The actual class to create a rectangle

		Attributes:
			width: rectangle width (integer).
			height: rectangle height (integer).
			number_of_instances: track instances(integer)
	"""
		self.height = height
		self.width = width
		type(self).number_of_instances += 1

	@property
	def width(self):
		"""check the current width

		Returns:
			width: of the rectangle
		"""
		return self.__width

	@property
	def height(self):
		"""check the current height

		Returns:
			height: of the rectangle
		"""
		return self.__height

	@width.setter
	def width(self, value):
		"""Property setter for width of rectangle.

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
		"""Calculates area of the rectangle.

		Return:
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
				rectangle.append(str(self.print_symbol))
			rectangle.append("\n")

		rectangle.pop()

		return "".join(rectangle)

	def __repr__(self):
		"""display rectangle as a string

		Returns:
			rectangle as a string
		"""
		return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

	def __del__(self):
		"""Destroys a class instance
		"""
		print("{:s}".format("Bye rectangle..."))
		type(self).number_of_instances -= 1


	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		"""Check larger rectangle by comparing the
		calculated area

		Args:
			rect_1: one rect instance
			rect_2: second rect instance

		Returns:
			Rectangle: the larger of the two rectangles
		"""
		if not isinstance(rect_1, Rectangle):
			raise TypeError("rect_1 must be an instance of Rectangle")

		if not isinstance(rect_2, Rectangle):
			raise TypeError("rect_2 must be an instance of Rectangle")

		area_1 = rect_1.area()
		area_2 = rect_2.area()

		if area_1 >= area_2:
			return rect_1

		return rect_2
