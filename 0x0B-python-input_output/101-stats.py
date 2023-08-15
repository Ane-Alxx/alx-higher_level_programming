#!/usr/bin/python3
"""

Module for task 101
101-stats.py

"""


def print_stats(size, st_cd):
	"""some informations
	"""
	print("File size: {}".format(size))
	for y in sorted(st_cd):
		print("{}: {}".format(y, st_cd[y]))


if __name__ == "__main__":
	import sys

	size = 0
	st_cd = {}
	v_cd = ['200', '301', '400', '401', '403', '404', '405', '500']
	track = 0

	try:
		for d in sys.stdin:
			if track == 10:
				print_stats(size, st_cd)
				track = 1
			else:
				track += 1

			d = d.split()

			try:
				size += int(d[-1])
			except (IndexError, ValueError):
				pass

			try:
				if d[-2] in v_cd:
					if st_cd.get(d[-2], -1) == -1:
						st_cd[d[-2]] = 1
					else:
						st_cd[d[-2]] += 1
			except IndexError:
				pass

		print_stats(size, st_cd)

	except KeyboardInterrupt:
		print_stats(size, st_cd)
		raise
