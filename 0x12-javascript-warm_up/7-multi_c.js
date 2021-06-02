#!/usr/bin/node
if (isNaN(process.argv[2]) === false) {
  for (let texts = 0; texts < process.argv[2]; texts++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
