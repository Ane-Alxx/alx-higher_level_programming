#!/usr/bin/node
//this is a code solution for task 100
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
