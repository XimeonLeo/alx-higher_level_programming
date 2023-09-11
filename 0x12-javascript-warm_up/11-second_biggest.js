#!/usr/bin/node


const arr = process.argv.slice(2);
if (arr.length < 2) {
  console.log(0);
} else {
  let array = arr.map(x => parseInt(x));
  let max = Math.max(...array);
  array = array.filter(y => y < max);
  max = Math.max(...array);
  console.log(max);
}

/* else {
 *   const array = arr.sort((a, b) => b - a); sorts the array desc
 *   const max = array[1];
 *   console.log(max);
 *   }
 */
