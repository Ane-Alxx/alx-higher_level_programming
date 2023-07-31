#!/usr/bin/python3

import sys


def safe_function(fct, *args):
	"""function from the advanced1
	"""
	try:
		answer = fct(*args)
		return (answer)
	except:
		print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
		return (None)
