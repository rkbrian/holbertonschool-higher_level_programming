#!/usr/bin/node
const add1 = process.argv[2];
const add2 = process.argv[3];
if (Number.isInteger(Number(add1)) && Number.isInteger(Number(add2))) {
  console.log(Number(add1) + Number(add2));
} else {
  console.log('NaN');
}
