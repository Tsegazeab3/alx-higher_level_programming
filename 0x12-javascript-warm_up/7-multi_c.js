#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2]) {
  const x = parseInt(argv[2]);
  if (isNaN(x)) {
    console.log('Missing number of occurrences');
  } else {
    let i = 0;
    while (i < x) {
      console.log('C is fun');
      i++;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
