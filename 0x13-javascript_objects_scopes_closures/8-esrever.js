#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let len = list.length;
  while (len > 0) {
    revList.push(list[len - 1]);
    len--;
  }
  return revList;
};
