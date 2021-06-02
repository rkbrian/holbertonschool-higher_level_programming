#!/usr/bin/node
let factNum = process.argv[2];
if (Number.isInteger(Number(factNum))) {
  function factorialize(factNum) {
    if (factNum === 0)
      return 1;
    else if (factNum < 0)
      return 0;
    else
      return (factNum * factorialize(factNum - 1));
  }
  console.log(factorialize(factNum));
} else if (factNum === 'NaN' || !process.argv[2]) {
  console.log(1);
}
