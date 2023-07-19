#!/usr/bin/python3

def complex_delete(a_dictionary, value):
	li = list(a_dictionary.keys())
	
	for v in li:
		if value == a_dictionary.get(v):
			del a_dictionary[v]

	return (a_dictionary)
