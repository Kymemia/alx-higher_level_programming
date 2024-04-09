#!/usr/bin/node
const args = process.argv.slice(2);

function addArgs (x, y) {
  return x + y;
}

if (args.length === 0) {
  console.log('NaN');
} else if (args.length > 1) {
  const sum = addArgs(parseInt(args[0]), parseInt(args[1]));
  console.log(sum);
} else {
  console.log('NaN');
}
