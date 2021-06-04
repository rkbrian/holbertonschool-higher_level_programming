#!/usr/bin/node
// Write a class Square that defines a square and
//   inherits from Square of 5-square.js
// Create an instance method called charPrint(c)
//   that prints the rectangle using the character c

// importing Square from file
const Squara = require('./5-square');
// Square as the extension of the old Square
class Square extends Squara {
  charPrint (c) {
    let ctext = c;
    if (typeof c === 'undefined') {
      ctext = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      const whatext = ctext.repeat(this.width);
      console.log(whatext);
    }
  }
}
module.exports = Square;
