#!/usr/bin/node
const arg_value = process.argv[2];
if (arg_value === undefined){
	console.log('No argument');
} else {
	console.log(arg_value);
}
