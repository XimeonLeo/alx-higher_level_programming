#!/usr/bin/node


function factorial (dgt) {
  if ((dgt === 0) || isNaN(dgt)) {
    return 1;
  } else {
    return dgt * factorial(dgt - 1);
  }
}

const number = parseInt(process.argv[2]);
console.log(factorial(number));
