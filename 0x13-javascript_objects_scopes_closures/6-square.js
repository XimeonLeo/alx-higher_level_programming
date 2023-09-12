#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const symbol = c.repeat(this.height);
      for (let i = 0; i < this.height; i++) {
        console.log(symbol);
      }
    }
  }
}

module.exports = Square;
