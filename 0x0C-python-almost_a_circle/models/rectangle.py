#!/usr/bin/python3
"""

Module for rectangle
"""

from models.base import Base


class Rectangle(Base):
		"""our rectaangle class for rect objects"""

		def __init__(self, width, height, x=0, y=0, id=None):
				super().__init__(id)
				if type(width) is not int:
						raise TypeError("width must be an integer")
				if width <= 0:
						raise ValueError("width must be > 0")
				self.__width = width
				if type(height) is not int:
						raise TypeError("height must be an integer")
				if height <= 0:
						raise ValueError("height must be > 0")
				self.__height = height
				if type(x) is not int:
						raise TypeError("x must be an integer")
				if x < 0:
						raise ValueError("x must be >= 0")
				self.__x = x
				if type(y) is not int:
						raise TypeError("y must be an integer")
				if y < 0:
						raise ValueError("y must be >= 0")
				self.__y = y

		@property
		def width(self):
				"""widdth getter method"""
				return self.__width

		@width.setter
		def width(self, width):
				"""width setter method"""
				if type(width) is not int:
						raise TypeError("width must be an integer")
				if width <= 0:
						raise ValueError("width must be > 0")
				self.__width = width

		@property
		def height(self):
				"""height getter method"""
				return self.__height

		@height.setter
		def height(self, height):
				"""height setter method"""
				if type(height) is not int:
						raise TypeError("height must be an integer")
				if height <= 0:
						raise ValueError("height must be > 0")
				self.__height = height

		@property
		def x(self):
				"""x getter method"""
				return self.__x

		@x.setter
		def x(self, x):
				"""x setter method"""
				if type(x) is not int:
						raise TypeError("x must be an integer")
				if x < 0:
						raise ValueError("x must be >= 0")
				self.__x = x

		@property
		def y(self):
				"""y getter method"""
				return self.__y

		@y.setter
		def y(self, y):
				"""y setter method"""
				if type(y) is not int:
						raise TypeError("y must be an integer")
				if y < 0:
						raise ValueError("y must be >= 0")
				self.__y = y

		def area(self):
				"""get area of rect"""
				return self.__width * self.__height

		def display(self):
				"""rectand to stdout"""
				for i in range(self.__y):
						print()
				for i in range(self.__height):
						for j in range(self.__x):
								print(' ', end='')
						for j in range(self.__width):
								print('#', end='')
						print()

		def __str__(self):
				return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}' \
								f' - {self.__width}/{self.__height}'

		def update(self, *args, **kwargs):
				"""Update rectangle attributes"""
				if args is not None and len(args) > 0:
						keylist = ["id", "width", "height", "x", "y"]
						for i in range(len(args)):
								setattr(self, keylist[i], args[i])
				elif kwargs is not None:
						for key, value in kwargs.items():
								setattr(self, key, value)

		def to_dictionary(self):
				"""dict rep of a rectangle"""
				return {"x": self.x, "y": self.y, "id": self.id,
								"height": self.height, "width": self.width}
