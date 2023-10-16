#!/usr/bin/node
const arg_values = process.argv.slice(2);
if (arg_values[0] && arg_values[1]) {
	console.log(`${arg_values[0]}` + ' is ' + `${arg_values[1]}`);
} else if (arg_values[0] && !arg_values[1]) {
	console.log(`${arg_values[0]}` + ' is ' + 'undefined');
} else {
	console.log('undefined is undefined');
}
