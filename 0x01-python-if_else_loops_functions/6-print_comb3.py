#!/usr/bin/python3

for symb1 in range(0, 10):
	for symb2 in range(symb1 + 1, 10):
		if symb1 == 8 and symb2 == 9:
			print("{}{}".format(symb1, symb2))
		else:
			print("{}{}".format(symb1, symb2), end=", ")
