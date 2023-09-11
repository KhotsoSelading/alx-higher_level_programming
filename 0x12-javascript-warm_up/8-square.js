#!/usr/bin/node
const iParser = parseInt(process.argv[2]);
if (!isNaN(iParser)) {
  for (let iParser = 0; iParser < n; iParser++) {
    console.log('X'.repeat(n));
  }
} else {
  console.log('Missing size');
}
