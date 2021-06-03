#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arrayArg = process.argv;
  arrayArg.splice(0, 2);
  const arrayNum = arrayArg.map(Number);
  const index = arrayNum.indexOf(Math.max(...arrayNum));
  arrayNum.splice(index, 1);
  console.log(Math.max(...arrayNum));
}
