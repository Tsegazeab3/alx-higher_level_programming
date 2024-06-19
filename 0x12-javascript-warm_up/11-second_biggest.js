#!/usr/bin/node
const { argv } = require('node:process');
const arr = argv.slice(2).map(Number);
if (arr.length < 2) {
  console.log(0);
} else {
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
