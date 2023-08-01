#!/usr/bin/python3
"""This is the solution for task 6"""

class Square:
        """This is the class for the square"""

	def __init__(self, size=0, position=(0, 0)):
                """this is the square"""

		self.size = size
		self.position = position

	@property
	def size(self):
                """just getting the information
on the square params"""
		return (self.__size)

	@size.setter
	def size(self, value):
                """this is for the square size"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	@property
	def position(self):
                """this is for the sq position"""
		return (self.__position)

	@position.setter
	def position(self, value):
                """Still on the position business"""
		if (not isinstance(value, tuple) or
				len(value) != 2 or
				not all(isinstance(num, int) for num in value) or
				not all(num >= 0 for num in value)):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

	def area(self):
                """this is for the area"""
		return (self.__size * self.__size)

	def my_print(self):
                """this is for the display"""
		if self.__size == 0:
			print("")
			return

		[print("") for m in range(0, self.__position[1])]
		for m in range(0, self.__size):
			[print(" ", end="") for n in range(0, self.__position[0])]
			[print("#", end="") for o in range(0, self.__size)]
			print("")
