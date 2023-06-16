#!/usr/bin/node
const [,, arg] = process.argv;
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++) {
      process.stdout.write('X');
    }
    console.log("");
  }
}
