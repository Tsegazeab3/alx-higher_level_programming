#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2]) {
  const num = parseInt(argv[2]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
} else {
  console.log('Not a number');
}
