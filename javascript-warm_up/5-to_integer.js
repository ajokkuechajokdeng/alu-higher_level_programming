#!/usr/bin/node
const [,, a] = process.argv;

if (isNaN(a)) {
  console.log("Not a number");
} else {
  console.log("My number: ${a}");
}
