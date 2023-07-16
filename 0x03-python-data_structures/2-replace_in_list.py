#!/usr/bin/python3


#I guess this is the defining line
def replace_in_list(my_list, idx, element):
	if idx >= 0 and idx < len(my_list):
		my_list[idx] = element
	return (my_list)
