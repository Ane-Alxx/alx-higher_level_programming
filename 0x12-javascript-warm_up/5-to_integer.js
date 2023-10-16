#!/usr/bin/node
const arg_values = process.argv.slice(2);
if (isNaN(arg_values[0]) === false) {
	const ct = parseInt(arg_values[0]);
	console.log('My number: ' + ct);
} else {
	console.log('Not a number');
}
