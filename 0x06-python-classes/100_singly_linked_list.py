#!/usr/bin/python3
"""solution for the linked list"""


class Node:
	"""this be the node"""

	def __init__(self, data, next_node=None):
		"""creating a new node
		"""
		self.data = data
		self.next_node = next_node

	@property
	def data(self):
		"""the node data"""
		return (self.__data)

	@data.setter
	def data(self, value):
		"""still on the node data"""
		if not isinstance(value, int):
			raise TypeError("data must be an integer")
		self.__data = value

	@property
	def next_node(self):
		"""Get/set the next_node of the Node."""
		return (self.__next_node)

	@next_node.setter
	def next_node(self, value):
		if not isinstance(value, Node) and value is not None:
			raise TypeError("next_node must be a Node object")
		self.__next_node = value


class SinglyLinkedList:
	"""Represent a singly linked list."""

	def __init__(self):
		""" and theSingly Linked List."""
		self.__head = None

	def sorted_insert(self, value):
		"""Insert into theSingly Linked List.
		"""
		new = Node(value)
		if self.__head is None:
			new.next_node = None
			self.__head = new
		elif self.__head.data > value:
			new.next_node = self.__head
			self.__head = new
		else:
			contn = self.__head
			while (contn.next_node is not None and
					contn.next_node.data < value):
				contn = contn.next_node
			new.next_node = contn.next_node
			contn.next_node = new

	def __str__(self):
		"""Display list"""
		valz = []
		contn = self.__head
		while contn is not None:
			valz.append(str(contn.data))
			contn = contn.next_node
		return ('\n'.join(valz))
