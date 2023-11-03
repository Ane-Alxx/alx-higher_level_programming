#!/usr/bin/python3
"""
Code script for:
@ Task 10 - my_github
@
@

"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
	auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
	read_file = requests.get("https://api.github.com/user", auth=auth)
	print(read_file.json().get("id"))
