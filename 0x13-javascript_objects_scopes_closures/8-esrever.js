#!/usr/bin/node
//this is a code solution for task
exports.esrever = function (list) {
	return list.reduceRight(function (array, current) {
		array.push(current);
		return array;
	}, []);
};
