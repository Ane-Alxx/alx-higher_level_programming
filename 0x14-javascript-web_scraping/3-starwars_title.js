#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api/films';

const mov_id = process.argv[2];

request(`${baseUrl}/${mov_id}/`, (error, response, body) => {
  if (error) {
	console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
