#!/usr/bin/python3
"""
Code script for:
@ Task 6 - post_email
@
@

"""
import sys
import requests


if __name__ == "__main__":
	url = sys.argv[1]
	value = {"email": sys.argv[2]}

	read_file = requests.post(url, data=value)
	print(read_file.text)
