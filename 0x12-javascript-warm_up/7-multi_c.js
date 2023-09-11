#!/usr/bin/node
let iParser = parseInt(process.argv[2]);
if (!isNaN(iParser)) {
  for (iParser--; iParser >= 0; iParser--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
