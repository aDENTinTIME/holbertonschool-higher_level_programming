#!/usr/bin/node

const fs = require('fs');
const { spawn } = require('child_process');
const pi = spawn('/usr/bin/python3', ['hi.py']);

fs.writeFile('hi.py', 'from time import sleep\nsleep(2)\nprint("wow")', 'utf8', (err) => {
  if (err) console.log(err);
  else {
    pi.stdout.on('data', (data) => {
      console.log(`${data}`);
      console.log('funky');
    });
  }
});
