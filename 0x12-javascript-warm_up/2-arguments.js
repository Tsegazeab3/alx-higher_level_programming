#!/usr/bin/node
const { argv } = require('node:process');
let a = 0;
argv.forEach(() => { a++; });
if (a === 2) {
  console.log('No argument');
}
if (a === 3) {
  console.log('Argument found');
}
if (a > 3) {
  console.log('Arguments found');
}
