#!/usr/bin/node

const args = process.argv.slice(2);

if (!args[0]) {
  console.log('No argument');
} else if (!args[1]) {
  console.log(args[0]);
}