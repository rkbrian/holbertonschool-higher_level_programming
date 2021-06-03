#!/usr/bin/node
// Write a class Square that defines a square and
//   inherits from Square of 5-square.js
// Create an instance method called charPrint(c)
//   that prints the rectangle using the character c

// importing Square from file
const Squara = require('./4-rectangle');
// Square as the extension of the old Square
class Square extends Squara {
  charPrint = function (c) {
    if (typeof(c) === 'undefined') {
      const ctext = 'X';
    } else {
      const ctext = c;
    }
    for (let i = 0; i < this.size; i++) {
      ctext.repeat(this.size);
      console.log(ctext);
    }
};
module.exports = Square;
