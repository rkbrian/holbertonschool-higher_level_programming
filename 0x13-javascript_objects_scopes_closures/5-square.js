#!/usr/bin/node
// Write a class Square that defines a square and
//   inherits from Rectangle of 4-rectangle.js

// importing Rectangle from file
const Rectangle = require('./4-rectangle');
// Square as the extension of Rectangle
class Square extends Rectangle {
  constructor (size) {
    super();
    if (size > 0) {
      this.width = size;
      this.height = size;
    }
  }
}
module.exports = Square;
