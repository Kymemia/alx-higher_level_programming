#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const leDict = {};

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    let x = 0;
    while (x < data.length) {
      const element = data[x];
      if (element.completed === true) {
        if (leDict[element.userId]) {
          leDict[element.userId] += 1;
        } else {
          leDict[element.userId] = 1;
        }
      }
      x++;
    }
    console.log(leDict);
  }
});
