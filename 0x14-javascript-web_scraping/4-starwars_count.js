#!/usr/bin/node
const request = require('request');
const leUrl = process.argv[2];
const url = `${leUrl}`;
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  let x = 0;
  while (x !== -1) {
    x = body.indexOf('people/18', x);
    if (x !== -1) {
      count++;
      x += 'people/18'.length;
    }
  }
  console.log(count);
});
