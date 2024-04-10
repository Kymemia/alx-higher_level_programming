#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let tally = 0;

  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      tally++;
    }
  }
  return tally;
};
