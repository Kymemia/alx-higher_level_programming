#!/usr/bin/node

const args = process.argv.slice(2);

function factorial (x) {
  if (x === 0 || x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

if (args.length === 0) {
  console.log('1');
}

if (!isNaN(parseInt(args[0]))) {
  if (args.length === 1) {
    console.log(factorial(parseInt(args[0])));
  }
}
