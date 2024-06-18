#!/usr/bin/node

const argc = process.argv.length;
const checkArgc = 'Argument' + (argc > 3 ? 's' : '') + ' found';

if (argc > 2) {
  console.log(checkArgc);
} else {
  console.log('No argument');
}