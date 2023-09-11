#!/usr/bin/node


const occurrence = parseInt(process.argv[2]);
if (isNaN(occurrence)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < occurrence; x++) {
    console.log('C is fun');
  }
}
