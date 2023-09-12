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
      for (let j = 0; j < this.width; j++) {
        let symb = '';
        for (let i = 0; i < this.height; i++) {
          symb += 'C';
        }
        console.log(symb);
      }
    }
  }
}

module.exports = Square;
