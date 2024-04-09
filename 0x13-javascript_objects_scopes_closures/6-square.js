#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let x = 0; x < this.width; x++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
