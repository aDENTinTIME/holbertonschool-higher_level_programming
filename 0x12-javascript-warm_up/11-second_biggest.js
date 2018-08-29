#!/usr/bin/node

if (!process.argv[3]) {
  console.log(0);
} else {
  let liz = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  console.log(liz[1]);
}
