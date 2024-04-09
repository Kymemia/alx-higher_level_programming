#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  let secondMax = -Infinity;

  for (const x of args) {
    if (x < max && x > secondMax) {
      secondMax = x;
    }
  }

  if (secondMax === -Infinity) {
    console.log(0);
  } else {
    console.log(secondMax);
  }
}
