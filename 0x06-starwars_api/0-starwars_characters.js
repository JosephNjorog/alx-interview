#!/usr/bin/node
const request = require('request');
const process = require('process');

const URL = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];

request(URL + filmId + '/', (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  } else if (res.statusCode !== 200) {
    console.log('Error');
    return;
  }

  body = JSON.parse(body);

  const printed = [];
  const charactersLength = body.characters.length;

  for (let i = 0; i < charactersLength; i++) {
    request(body.characters[i], (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      } else if (res.statusCode !== 200) {
        console.log('Error');
        return;
      }

      body = JSON.parse(body);
      printed.push({ index: i, name: body.name });

      if (printed.length === charactersLength) {
        printed.sort((a, b) => a.index - b.index);

        for (let j = 0; j < printed.length; j++) {
          console.log(printed[j].name);
        }
      }
    });
  }
});
