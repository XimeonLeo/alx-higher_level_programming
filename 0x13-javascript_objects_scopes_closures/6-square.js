#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      const symbol = c.repeat(this.height);
      for (let i = 0; i < this.height; i++) {
        console.log(symbol);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
