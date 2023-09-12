#!/usr/bin/node

let valuePrinted = 0;
exports.logMe = function (item) {
  console.log(`${valuePrinted}: ${item}`);
  valuePrinted += 1;
};
