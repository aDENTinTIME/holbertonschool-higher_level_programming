#!/usr/bin/node

let firstArg = process.argv[2];

if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
