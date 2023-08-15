#!/usr/bin/python3
"""

Module for task 11
11-student.py

"""

class Student:
	"""A class to initialize 
	a student instance

	attributes:
		first_name: fname string
		last_name: lname string
		age: age integer
	"""
	first_name = " "

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

	def to_json(self, attrs=None):
		"""Just for the dictionary thingy again"""

		diction = {}
		if attrs is None:
			return self.__dict__
		for lem in attrs:
			if lem in self.__dict__:
				diction[lem] = self.__dict__[lem]
		return diction

	def reload_from_json(self, json):
		"""makes or stuff brand new"""

		for a, b in json.items(:
			setattr(self, a, b)
