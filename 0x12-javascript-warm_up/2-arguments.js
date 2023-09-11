#!/usr/bin/node
let a;
if (process.argv.length < 3) {
  a = 'No argument';
} else if (process.argv.length === 3) {
  a = 'Argument found';
} else {
  a = 'Arguments found';
}
console.log(a);
