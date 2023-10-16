#!/usr/bin/node

const arg_list = process.argv.slice(2);
if (arg_list.length === 0 || arg_list.length === 1) {
	console.log(0);
} else {
	arg_list.sort((a, b) => a - b);
	console.log(arg_list[arg_list.length - 2]);
}
