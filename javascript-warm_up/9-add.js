#!/usr/bin/node
const [,, arg1, arg2] = process.argv;
const a = parseInt(arg1);
const b = parseInt(arg2);
const add = (a, b) => {
  return (a + b);
};

console.log(add(a, b));
