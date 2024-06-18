#!/usr/bin/node
const argc = process.argv.length;
const checkArgc = 'Argument' + (argc > 3 ? 's' : '') + ' found';

argc > 2 ? console.log(checkArgc) : console.log('No argument');