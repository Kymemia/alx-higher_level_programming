#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (err, response, body) => {
      if (err) {
        reject(err);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const characterUrls = data.characters;
    const promises = characterUrls.map(getCharacter);
    Promise.all(promises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => console.error(err));
  }
});
