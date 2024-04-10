#!/usr/bin/node
const fs = require('fs');

const [fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileB, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }
    const result = data1 + data2;

    fs.writeFile(fileC, result, 'utf8', err=> {
      if (err) {
        console.error(err);
        return;
      }
    });
  });
});
