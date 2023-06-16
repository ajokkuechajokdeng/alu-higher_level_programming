#!/usr/bin/node
const [,, arg] = process.argv;

if (!arg) {
  console.log('No argument');
}else { console.log(arg); }
