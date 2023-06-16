#!/usr/bin/node

const add = (a, b) => {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
};

exports.add = add;
