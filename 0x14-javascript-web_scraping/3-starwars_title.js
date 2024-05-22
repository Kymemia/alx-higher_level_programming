#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
let episodeDict = {};
request.get(url, (err, response, body) => {
  if (err) {
    return console.error(err);
  } else {
    episodeDict = JSON.parse(body);
    console.log(episodeDict.title);
  }
});
