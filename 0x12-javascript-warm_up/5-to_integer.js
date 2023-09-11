#!/usr/bin/node
const iParser = parseInt(process.argv[2]);
if (!isNaN(iParser)) {
  console.log('My number: ' + iParser);
} else {
  console.log('Not a number');
}
