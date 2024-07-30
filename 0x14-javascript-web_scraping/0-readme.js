#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (err, content) => {
  err ? console.log(err) : console.log(content);
});
