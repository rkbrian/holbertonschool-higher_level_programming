#!/usr/bin/node
const factNum = process.argv[2];
function factorialize (factNum) {
  if (factNum === 0) {
    return (1);
  } else if (factNum < 0) {
    return (0);
  } else {
    return (factNum * factorialize(factNum - 1));
  }
}
if (Number.isInteger(Number(factNum))) {
  console.log(factorialize(factNum));
} else if (factNum === 'NaN' || !process.argv[2]) {
  console.log(1);
} else {
  console.log('Not an integer');
}
