#!/usr/bin/python3

"""

this is a module for the base class

"""

import json
import os
import csv
import turtle
import random


class Base():
		"""Start of the base class"""

		__nb_objects = 0

		def __init__(self, id=None):
				if id is not None:
						self.id = id
				else:
						Base.__nb_objects += 1
						self.id = self.__nb_objects

		@staticmethod
		def to_json_string(list_dictionaries):
				"""our return: the Json version of the dictionaries"""
				if list_dictionaries is None or len(list_dictionaries) == 0:
						return '[]'
				return json.dumps(list_dictionaries)

		@classmethod
		def save_to_file(cls, list_objs):
				"""Object files: json representation/version"""
				filename = cls.__name__ + '.json'
				with open(filename, 'w+') as my_file:
						my_list = []
						if list_objs is not None and len(list_objs) > 0:
								for pixel in list_objs:
										my_list.append(pixel.to_dictionary())
						my_file.write(cls.to_json_string(my_list))

		@staticmethod
		def from_json_string(json_string):
				"""List: from jason str"""
				if (json_string is None or len(json_string) == 0):
						return []
				else:
						return json.loads(json_string)

		@classmethod
		def create(cls, **dictionary):
				"""Dictionary as att returns an instance"""
				if cls.__name__ == 'Square':
						cont = cls(1)
				else:
						cont = cls(1, 1)
				cont.update(**dictionary)
				return cont

		@classmethod
		def load_from_file(cls):
				"""returns list of instances from json string"""
				my_list = []
				file_name = cls.__name__ + '.json'
				if os.path.exists(file_name) is True:
						with open(file_name, 'r') as my_file:
								my_list = cls.from_json_string(my_file.read())
						for i in range(len(my_list)):
								my_list[i] = cls.create(**my_list[i])
				return my_list

		@classmethod
		def save_to_file_csv(cls, list_objs):
				"""our guys inheriting from the csv"""
				file_name = cls.__name__ + '.csv'
				with open(file_name, "w+") as csvfile:
						if list_objs is None or len(list_objs) == 0:
								csvfile.write('[]')
						else:
								if cls.__name__ == 'Rectangle':
										fields = ['id', 'width', 'height', 'x', 'y']
								elif cls.__name__ == 'Square':
										fields = ['id', 'size', 'x', 'y']
								else:
										return
								writer = csv.DictWriter(csvfile, fieldnames=fields)
								writer.writeheader()
								for pixel in list_objs:
										writer.writerow(pixel.to_dictionary())

		@classmethod
		def load_from_file_csv(cls):
				"""Load list of object from a csv file"""
				my_list = []
				file_name = cls.__name__ + '.csv'
				if os.path.exists(file_name) is True:
						with open(file_name, "r") as csvfile:
								dictreader = csv.DictReader(csvfile)
								my_list = [dict([key, int(value)] for key, value
																in dictionary.items()) for dictionary
													 in dictreader]
						for i in range(len(my_list)):
								my_list[i] = cls.create(**my_list[i])
				return my_list

		@staticmethod
		def draw(list_rectangles, list_squares):
				"""turtle draw squares and rectangles"""
				colorlist = ('red', 'blue', 'purple', 'yellow', 'green', 'pink')
				pen_draw = turtle.Turtle()
				pen_draw.up
				pen_draw.penup()
				pen_draw.goto(-200, -200)
				for pixel in list_rectangles:
						pen_draw.penup()
						pen_draw.goto(-200 + pixel.x * 2 + 20, -200 + pixel.y * 2 + 20)
						pen_draw.color(random.choice(colorlist), random.choice(colorlist))
						pen_draw.begin_fill()
						for i in range(2):
								pen_draw.forward(pixel.width)
								pen_draw.left(90)
								pen_draw.forward(pixel.height)
								pen_draw.left(90)
						pen_draw.end_fill()
				for pixel in list_squares:
						pen_draw.penup()
						pen_draw.goto(-200 + pixel.x * 2 + 20, -200 + pixel.y * 2 + 20)
						pen_draw.color(random.choice(colorlist), random.choice(colorlist))
						pen_draw.begin_fill()
						for i in range(4):
								pen_draw.forward(pixel.size)
								pen_draw.left(90)
						pen_draw.end_fill()
				turtle.exitonclick()
