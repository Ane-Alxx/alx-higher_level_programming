#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const my_file = process.argv[2];

fs.readFile(my_file, 'utf8', function (err, data) {

  if (err) {
	console.log(err);
  } else {
	process.stdout.write(data);
  }
});
