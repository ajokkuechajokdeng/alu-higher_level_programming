#!/usr/bin/node
const [,, a] = process.argv;
if (!isNaN(a)) {
  for (let i = 0; i < a; i++) {
    console.log('C is fun');
  }
} 
else { console.log('Missing number of occurencess'); }
