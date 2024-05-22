#!/usr/bin/node

const fs = require('fs').promises;
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8')
  .then(data => console.log(data))
  .catch(err => console.error(err));
