#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
	"""function to divide two lists 
	based on each element in the list
	"""
	sol_list = []

	for b in range(0, list_length):
		try:
			answer = my_list_1[b] / my_list_2[b]
		except(TypeError, ZeroDivisionError):
			print("wrong type")
			answer = 0
		except IndexError:
			print("out of range")
			answer = 0
		finally:
			sol_list.append(answer)
	return (sol_list)
