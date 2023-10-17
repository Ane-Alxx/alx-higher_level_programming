#!/usr/bin/node
//this is a code solution for task 2
module.exports = class Rectangle {
	constructor (w, h) {
	if (w > 0 && h > 0) { 
		this.width = w;
		this.height = h; 
	}
	}
}
