#!/usr/bin/python3
"""

Module for task 9
9-student.py

"""

class Student:
	"""A class to initialize 
	a student instance"""

	def __init__(self, first_name, last_name, age):
		"""The initialisation attributes for class
		student

		attributes:
			first_name: firstname
			last_name: lastname
			age: age
		"""

		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self):
		"""returns a whole as dictionary because
		we can"""

		return self.__dict__
