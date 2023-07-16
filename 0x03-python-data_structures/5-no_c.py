#!/usr/bin/python3

def no_c(my_string):
	duplicate = [cp for cp in my_string if cp != 'c' and cp != 'C']
	return ("".join(duplicate))
