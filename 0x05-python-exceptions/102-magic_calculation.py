#!/usr/bin/python3


def magic_calculation(a, b):
	"""function from the advanced1
	"""
	
	answer = 0

	for k in range(1, 3):
		try:
			if k > a:
				raise Exception('Too far')
			else:
				answer += a ** b / k
		except:
			answer = b + a
			break
	return (answer)
