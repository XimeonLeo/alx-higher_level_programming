#!/usr/bin/node
// prints all characters of a Star Wars movie:

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(character => {
    request.get(character, (err, res, data) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(data).name);
    });
  });
});
