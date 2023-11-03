#!/usr/bin/python3
"""

Code script for:
@ Task 8 - json_api
@
@

"""
import sys
import requests


if __name__ == "__main__":
	letter = "" if len(sys.argv) == 1 else sys.argv[1]
	payload = {"q": letter}

	read_file = requests.post("http://0.0.0.0:5000/search_user", data=payload)
	try:
		response = read_file.json()
		if response == {}:
			print("No result")
		else:
			print("[{}] {}".format(response.get("id"), response.get("name")))
	except ValueError:
		print("Not a valid JSON")
