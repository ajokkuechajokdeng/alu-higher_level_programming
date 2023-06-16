#!/usr/bin/node
const [,, arg] = process.argv;
function rec (arg) {
  if (arg >= 1) {
    return arg * rec(arg - 1);
  } else return 1;
}

console.log(rec(arg));
