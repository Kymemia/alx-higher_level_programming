#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];
const fileStream = fs.createWriteStream(filepath);

request.get(url)
  .on('error', err => console.error(err))
  .pipe(fileStream)
  .on('finish', () => {})
  .on('error', err => console.log(err));
