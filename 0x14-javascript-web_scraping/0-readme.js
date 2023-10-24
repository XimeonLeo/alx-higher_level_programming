#!/usr/bin/node
// a script that reads from a file and prints its content
const fs = require('fs');

// Path to the file to read
const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
