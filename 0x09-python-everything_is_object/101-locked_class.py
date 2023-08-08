#!/usr/bin/python3
"""Locked class definition"""


class LockedClass:
	"""
	A class that doesn't allow the user to dynamically instance
	new attributes

	Attributes:
		first_name: a string firstname
	"""

	__slots__ = ["first_name"]

	def __init__(self):
		"""Instance the locked class"""

		self.first_name = "first_name"
