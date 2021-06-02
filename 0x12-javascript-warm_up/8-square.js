#!/usr/bin/node
if (isNaN(process.argv[2]) === false) {
  for (let rows = 0; rows < process.argv[2]; rows++) {
    let Xtext = '';
    for (let columns = 0; columns < process.argv[2]; columns++) {
      Xtext += 'X';
    }
    console.log(Xtext);
  }
} else {
  console.log('Missing size');
}
