#!/usr/bin/node
// prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, res, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const movies = JSON.parse(data).results;
  const wedgeAntiles = movies.filter((movie) => movie.characters.includes(character));
  console.log(`${wedgeAntiles.length}`)
})
