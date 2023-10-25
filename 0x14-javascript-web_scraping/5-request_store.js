#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

const request = require('request');
const url = process.argv[2];

const fs = require('fs');
const filePath = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  // This block writes into the file if GET was succesful
  fs.writeFile(filePath, body, { flag: 'w' }, (error) => {
    if (error) {
      console.error(error);
    }
  });
});
