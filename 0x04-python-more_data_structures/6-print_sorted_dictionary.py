#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

	dicco = list(a_dictionary.keys())
	dicco.sort()

	for a in dicco:
		print("{}: {}".format(a, a_dictionary.get(a)))
