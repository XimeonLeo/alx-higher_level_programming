#!/usr/bin/node
// A script that write a string into a file
const fs = require('fs');

// The path to the file
const filePath = process.argv[2];

// String to write
const content = process.argv[3];

fs.writeFile(filePath, content, { flag: 'w' }, (err) => {
  if (err) {
    console.error(err);
  }
});
