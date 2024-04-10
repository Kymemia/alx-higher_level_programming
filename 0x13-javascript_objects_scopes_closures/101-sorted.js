#!/usr/bin/node
const data = require('./101-data').dict;

const usersByOccurrence = {};
for (const user in data) {
  const occurrences = data[user];
  if (!(occurrences in usersByOccurrence)) {
    usersByOccurrence[occurrences] = [];
  }
  usersByOccurrence[occurrences].push(parseInt(user));
}
console.log(usersByOccurrence);
