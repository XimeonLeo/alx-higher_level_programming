#!/usr/bin/node

const dict = require('./101-data').dict;
const myDict = {};

for (const id in dict) {
  const val = dict[id];
  if (val in myDict) {
    myDict[val].push(id);
  } else {
    myDict[val] = [id];
  }
}
console.log(myDict);
