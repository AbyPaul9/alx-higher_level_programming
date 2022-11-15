#!/usr/bin/node
const request = require('request');

let movieNb = 0;

if (process.argv.length === 3) {
  request(process.argv[2], { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }
    body.results.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.indexOf('people/18') >= 0) {
          movieNb = movieNb + 1;
        }
      });
    });
    console.log(movieNb);
  });
}
