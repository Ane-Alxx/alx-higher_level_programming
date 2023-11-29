#!/usr/bin/node
const request = require('request');

const baseURL = process.argv[2];
request(baseURL, (error, response, body) => {
  const avgg = {};
  if (error) {
	console.log(error);
  }
  const json = JSON.parse(body);
  json.forEach(element => {
	if (element.completed) {
	  if (!avgg[element.userId]) {
		avgg[element.userId] = 0;
	  }
	  avgg[element.userId]++;
	}
  });
  console.log(avgg);
});
