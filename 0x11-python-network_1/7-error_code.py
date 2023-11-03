#!/usr/bin/python3
"""
Code script for:
@ Task 7 - eeror_code
@
@

"""
import sys
import requests


if __name__ == "__main__":
	url = sys.argv[1]

	read_file = requests.get(url)
	if read_file.status_code >= 400:
		print("Error code: {}".format(read_file.status_code))
	else:
		print(read_file.text)
