#!/usr/bin/node
//  a script that prints a square
const iParser = parseInt(process.argv[2]);
if (!isNaN(iParser)) {
  for (let i = 0; i < iParser; i++) {
    console.log('X'.repeat(iParser));
  }
} else {
  console.log('Missing size');
}
