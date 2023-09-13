#!/usr/bin/node

const _Square = require('./5-square');

class Square extends _Square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let j = 0; j < this.width; j++) {
        let symb = '';
        for (let i = 0; i < this.height; i++) {
          symb += c;
        }
        console.log(symb);
      }
    }
  }
}

module.exports = Square;
