#!/usr/bin/node
const request = require('request');

const movieUrl = 'https://swapi-api.hbtn.io/api/films/';
const characterUrl = 'https://swapi-api.hbtn.io/api/people/';
const charactersList = [];

if (process.argv.length === 3) {
  request(movieUrl + process.argv[2], { json: true }, (err, res, body) => {
    if (err) { return console.error(err); }
    body.characters.forEach(character => {
      const characterId = character.split('/')[5];

      request(characterUrl + characterId, { json: true }, (err, res, body) => {
        if (err) { return console.error(err); }
        console.log(body.name);
        charactersList.push(body.name);
      });
    });
  });
}
