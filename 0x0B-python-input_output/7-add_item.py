#!/usr/bin/python3
"""

Module for task 7
7-add_item.py

"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_items = []
if os.path.exists("add_item.json"):
	file_items = load_from_json_file("add_item.json")
save_to_json_file(file_items + sys.argv[1:], "add_item.json")
