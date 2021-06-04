#!/usr/bin/node
// Write a function that prints the number of arguments
//   already printed and the new argument value
let printLine = -1;
exports.logMe = function (item) {
  if (item) {
    printLine++;
    console.log(printLine + ': ' + item);
  }
};
