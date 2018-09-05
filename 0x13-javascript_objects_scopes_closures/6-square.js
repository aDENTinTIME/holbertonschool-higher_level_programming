#!/usr/bin/node

const SquareDaddy = require('./5-square');

module.exports = class Square extends SquareDaddy {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        process.stdout.write(c || 'X');
      }
      console.log();
    }
  }
};
