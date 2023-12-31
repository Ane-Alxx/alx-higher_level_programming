#!/usr/bin/python3
"""
Code script for:
@ Task 3 - error_code
@
@

"""
import urllib.request
import urllib.error

if __name__ == "__main__":
	"""Just doing this again because being extra hurts no one"""
	import sys
	from urllib import request, error

	try:
		with request.urlopen(sys.argv[1]) as r:
			print(r.read().decode('UTF-8'))
	except error.HTTPError as er:
		print('Error code:', er.code)
