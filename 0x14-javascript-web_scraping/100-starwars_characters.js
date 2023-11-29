#!/usr/bin/node
import requests

# Function to get characters from a Star Wars movie
def get_movie_characters(movie_id):
	# Base URL for Star Wars API
	base_url = "https://swapi.dev/api/films/"

	# Construct the URL for the specific movie
	movie_url = f"{base_url}{movie_id}"

	# Send a GET request to the Star Wars API
	response = requests.get(movie_url)

	# Check if the request was successful
	if response.status_code == 200:
		# Get the JSON data from the response
		movie_data = response.json()

		# Extract the character names from the JSON data
		characters = [character["name"] for character in movie_data["characters"]]

		# Print the character names
		for character in characters:
			print(character)
	else:
		print(f"Error: Failed to retrieve movie data. Status code: {response.status_code}")

# Get the movie ID from the user
movie_id = int(input("Enter the movie ID (example: 3 for Return of the Jedi): "))

# Get and print the characters for the specified movie
get_movie_characters(movie_id)
