#!/usr/bin/python3

def uniq_add(my_list=[]):
	ooak = set(my_list)
	val = 0

	for a in ooak:
		val += a

	return (val)
