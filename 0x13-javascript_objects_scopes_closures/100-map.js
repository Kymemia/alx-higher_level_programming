#!/usr/bin/node
const { list } = require('./100-data');

const leList = list.map((value, index) => value * index);
console.log(list);
console.log(leList);
