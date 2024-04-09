#!/usr/bin/node
const args = process.argv.slice(2);

if (!isNaN(parseInt(args[0]))) {
  const iter = parseInt(args[0]);
  for (let x = 0; x < iter; x++) {
    let row = '';
    for (let y = 0; y < iter; y++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
