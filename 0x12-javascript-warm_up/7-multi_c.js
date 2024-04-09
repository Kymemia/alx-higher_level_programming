#!/usr/bin/node
const args = process.argv.slice(2);

if (!isNaN(parseInt(args[0]))) {
  const iter = parseInt(args[0]);
  for (let x = 0; x < iter; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
