#!/usr/bin/node
exports.esrever = function (list) {
  const buf = [];

  for (let x = list.length - 1; x >= 0; x--) {
    buf.push(list[x]);
  }

  return buf;
};
