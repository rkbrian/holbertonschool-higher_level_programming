#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
// <class> notation, takes 2 arguments of width and height
// instance method <print()> to print the rectangle using <X>
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
// instance method print()
Rectangle.prototype.print = function () {
  for (let i = 0; i < this.height; i++) {
    const xtext = 'X'.repeat(this.width);
    console.log(xtext);
  }
};
module.exports = Rectangle;
