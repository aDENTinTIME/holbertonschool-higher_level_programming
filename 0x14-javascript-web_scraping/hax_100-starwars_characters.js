#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
let names = {};

function getChar(charUrl) {
  request.get(charUrl, (error, response, body) => {
    return JSON.parse(body).name;
  });
}

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    for (const key in JSON.parse(body).characters) {
      names[JSON.parse(body).characters[key]] = getChar(JSON.parse(body).characters[key]);
    }
  }
});

function printUs(names) {
  for (key in Object.keys(names)) {
    console.log(names[key]);
  }
}

const fs = require('fs');
const { spawn } = require('child_process');
const pi = spawn('/usr/bin/python3', ['hi.py']);

fs.writeFile('hi.py', 'from time import sleep\nsleep(9)\nprint("wow")', 'utf8', (err) => {
  if (err) console.log(err);
  else {
    pi.stdout.on('data', (data) => {
      printUs(names);
    });
    pi.stderr.on('data', (data) => {
      printUs(names);
    });
    pi.on('exit', (code) => {
      printUs(names);
    });
  }
});
