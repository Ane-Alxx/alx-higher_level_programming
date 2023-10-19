#!/usr/bin/node
//this is a code solution for task 7
exports.nbOccurences = function (list, searchElement) {
	return list.reduce((itr_count, current) => current === searchElement ? itr_count + 1 : itr_count, 0);
};
