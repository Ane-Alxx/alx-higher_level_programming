#!/usr/bin/python3
"""
Code script for:
@ Task 5 - hbtn_header
@
@

"""
import sys
import requests


if __name__ == "__main__":
	url = sys.argv[1]

	read_file = requests.get(url)
	print(read_file.headers.get("X-Request-Id"))
