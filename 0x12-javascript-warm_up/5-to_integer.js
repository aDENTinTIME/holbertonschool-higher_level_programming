#!/usr/bin/node

let firstArg = parseInt(process.argv[2], 10);

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstArg);
}
