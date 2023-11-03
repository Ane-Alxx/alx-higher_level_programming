#!/usr/bin/python3
"""
Code script for:
@ Task 100 -github_commits
@
@
"""
import sys
import requests


if __name__ == "__main__":
	url = "https://api.github.com/repos/{}/{}/commits".format(
		sys.argv[2], sys.argv[1])

	read_file = requests.get(url)
	commits = read_file.json()
	try:
		for k in range(10):
			print("{}: {}".format(
				commits[k].get("sha"),
				commits[k].get("commit").get("author").get("name")))
	except IndexError:
		pass
