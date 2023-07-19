#!/usr/bin/python3

def multiply_by_2(a_dictionary):
	dirt = a_dictionary.copy()
	key_list = list(dirt.keys())

	for a in key_list:
		dirt[a] *= 2

	return (dirt)
