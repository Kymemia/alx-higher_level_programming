#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      return 'Rectangle {}';
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.width || !this.height) {
      return;
    }
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const buf = this.width;
    this.width = this.height;
    this.height = buf;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
