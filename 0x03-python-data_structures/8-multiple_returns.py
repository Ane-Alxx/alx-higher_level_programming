#!/usr/bin/python3
# this is the code for task 8


def multiple_returns(sentence):
	"""The instructions are written in the project question"""
	if sentence == "":
		return (0, None)
	return (len(sentence), sentence[0])
