#!/usr/bin/node

const args = process.argv.slice(2);

if (!args[0]) {
  console.log('No argument');
} else {
  const parts = args[0].split(' ');
  console.log(parts[0]);
}
