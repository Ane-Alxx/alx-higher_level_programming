#!/usr/bin/python3
"""comment placeholder"""


def find_peak(list_of_integers):
	"""comment place holder"""

	if list_of_integers is None or list_of_integers == []:
		return None
	low_val = 0
	high_val = len(list_of_integers)
	midpoint_val = ((high_val - low_val) // 2) + low_val
	midpoint_val = int(midpoint_val)
	if high_val == 1:
		return list_of_integers[0]
	if high_val == 2:
		return max(list_of_integers)
	if list_of_integers[midpoint_val] >= list_of_integers[midpoint_val - 1] and\
			list_of_integers[midpoint_val] >= list_of_integers[midpoint_val + 1]:
		return list_of_integers[midpoint_val]
	if midpoint_val > 0 and list_of_integers[midpoint_val] < list_of_integers[midpoint_val + 1]:
		return find_peak(list_of_integers[midpoint_val:])
	if midpoint_val > 0 and list_of_integers[midpoint_val] < list_of_integers[midpoint_val - 1]:
		return find_peak(list_of_integers[:midpoint_val])
