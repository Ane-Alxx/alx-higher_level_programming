#!/usr/bin/python3
"""function for text indentation"""


def text_indentation(text):
	"""function takes in a single argument

	arg:
		text: the value that will be passed in"""
	if not isinstance(text, str):
		raise TypeError("text must be a string")

	for delimeter in "?:.":
		txts = (delimeter + "\n\n").join(
				[index.strip(" ") for index in txts.split(delimeter)])


if __name__ == "__main__":
	import doctest
	doctest.testfile("tests/5-text_indentation.txt")
