#!/usr/bin/python3
for combi in range(0, 100):
	if combi == 99:
		print("{}".format(combi))
	else:
		print("{:02}".format(combi), end=", ")
