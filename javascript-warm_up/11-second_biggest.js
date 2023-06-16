#!/usr/bin/node

const [,, ...args] = process.argv;
if (args.length === 1 || args.length === 0) {
  console.log(0);
} else {
  args.sort(function (a, b) { return b - a; });
  const uniqueArgs = [...new Set(args)];
  const [, y] = [...uniqueArgs];
  console.log(y);
}
