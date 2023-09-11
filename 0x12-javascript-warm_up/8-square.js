#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let height = 0; height < size; height++) {
    let print = '';
    for (let width = 0; width < size; width++) {
      print += 'X';
    }
    console.log(`${print}`);
  }
}
