#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// <class> notation, takes 2 arguments of width and height
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
