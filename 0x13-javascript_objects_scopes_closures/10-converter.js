#!/usr/bin/node

exports.converter = function (base) {
  return dgt => dgt.toString(base);
};
