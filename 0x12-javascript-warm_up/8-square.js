#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

if (isNaN(x)) {
  console.log('Missing size');
  process.exit();
}

let str = '';

for (let col = 0; col < x; col++) {
  str += 'X';
}
for (let row = 0; row < x; row++) {
  console.log(str);
}
