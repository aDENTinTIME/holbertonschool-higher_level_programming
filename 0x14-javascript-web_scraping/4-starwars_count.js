#!/usr/bin/node

const request = require('request');
const WedgeAntilles = '18';
const characters = '?characters=';
const url = process.argv[2] + characters + WedgeAntilles;
let count = 0;

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    for (const key in JSON.parse(body).results) {
      for (const key2 in JSON.parse(body).results[key]) {
        if (key2 === 'characters') {
          for (const key3 in JSON.parse(body).results[key][key2]) {
            if (JSON.parse(body).results[key][key2][key3].includes('18')) {
              count++;
              // console.log(JSON.parse(body).results[key][key2][key3]);
            }
          }
        }
      }
    }
  }
  console.log(count);
});
