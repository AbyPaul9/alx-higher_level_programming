#!/usr/bin/node
const request = require('request');

const movieUrl = 'https://swapi-api.hbtn.io/api/films/';

function printCharacterNameOfMovie (movieId) {
  request(movieUrl + movieId, { json: true }, async (err, response, body) => {
    if (err) { return console.error(err); }

    // Be carefull, foreach, because it use a callback it's considered like a function
    // So you can't use it with an await
    for (const characterUrl of body.characters) {
      // A promise is an object which can be returned synchronously from an asynchronous function (ref).
      // The purpose of async/await functions is to simplify the behavior of using promises synchronously
      // and to perform some behavior on a group of Promises. Just as Promises are similar to structured
      // callbacks, async/await is similar to combining generators and promises. Async functions always
      // return a Promise.
      const name = await new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (err, response, body) => {
          if (err) { return reject(err); }

          resolve(body.name);
        });
      });
      if (name !== undefined) console.log(name);
    }
  });
}

if (process.argv.length === 3) {
  printCharacterNameOfMovie(process.argv[2]);
}
