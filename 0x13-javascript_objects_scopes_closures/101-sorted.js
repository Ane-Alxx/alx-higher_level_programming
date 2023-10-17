#!/usr/bin/node
//this is a code solution for task 101
const dict = require('./101-data').dict;

const big_list = Object.entries(dict);
const val_dict = Object.values(dict);
const val_niq = [...new Set(val_dict)];
const newDict = {};
for (const t in val_niq) {
	const list = [];
	for (const s in big_list) {
		if (big_list[s][1] === val_niq[t]) {
			list.unshift(big_list[s][0]);
		}
	}
	newDict[val_niq[t]] = list;
}
console.log(newDict);
